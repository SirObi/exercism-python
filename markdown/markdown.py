import re
from collections import OrderedDict

OPENING_TAG = '<'
CLOSING_TAG= '</'
HEADERS = OrderedDict({'######': 'h6',
                       '#####': 'h5',
                       '####': 'h4',
                       '###:': 'h3',
                       '##': 'h2',
                       '#': 'h1'})


def detect_header_tags(l=''):
    for k,v in HEADERS.items():
        line_with_header = re.match(f'{k} (.*)', l)
        if line_with_header:
            rest_string = line_with_header.group(1)
            return OPENING_TAG + v + '>' + rest_string + CLOSING_TAG + v + '>'
    return l


def detect_bold_tags(l=''):
    line_with_bold = re.match('(.*)__(.*)__(.*)', l)
    if line_with_bold:
        return line_with_bold.group(1) + '<strong>' + \
            line_with_bold.group(2) + '</strong>' + line_with_bold.group(3)
    return l


def detect_italic_tags(l=''):
    line_with_ital = re.match('(.*)_(.*)_(.*)', l)
    if line_with_ital:
        return line_with_ital.group(1) + '<em>' + \
            line_with_ital.group(2) + '</em>' + line_with_ital.group(3)
    return l


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        i = detect_header_tags(i)
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                curr = detect_bold_tags(curr)
                curr = detect_italic_tags(curr)
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                curr = detect_bold_tags(curr)
                curr = detect_italic_tags(curr)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        i = detect_bold_tags(i)
        i = detect_italic_tags(i)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
