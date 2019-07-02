import re
from collections import OrderedDict

OPENING_TAG = '<'
CLOSING_TAG= '</'
U_LIST = '<ul>{}</ul>'
HEADERS = OrderedDict({'######': 'h6',
                       '#####': 'h5',
                       '####': 'h4',
                       '###:': 'h3',
                       '##': 'h2',
                       '#': 'h1'})


def replace_header_tags(l=''):
    for k,v in HEADERS.items():
        line_with_header = re.match(f'{k} (.*)', l)
        if line_with_header:
            rest_string = line_with_header.group(1)
            return OPENING_TAG + v + '>' + rest_string + CLOSING_TAG + v + '>'
    return l


def replace_bold_tags(l=''):
    line_with_bold = re.match('(.*)__(.*)__(.*)', l)
    if line_with_bold:
        return line_with_bold.group(1) + '<strong>' + \
            line_with_bold.group(2) + '</strong>' + line_with_bold.group(3)
    return l


def replace_italic_tags(l=''):
    line_with_ital = re.match('(.*)_(.*)_(.*)', l)
    if line_with_ital:
        return line_with_ital.group(1) + '<em>' + \
            line_with_ital.group(2) + '</em>' + line_with_ital.group(3)
    return l


def catch_all_in_p_tag(l=''):
    return l if re.match('<h|<ul|<p|<li', l) else '<p>' + l + '</p>'

def check_if_list_item(l=''):
    list_item = re.match(r'\* (.*)', l)
    if list_item:
        return f'<li>{list_item.group(1)}</li>'
    return False


def is_last_line(i, _list):
    return _list.index(i) == len(_list) - 1


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    unordered_list = ''
    for i in lines:
        line = replace_header_tags(i)
        line = replace_bold_tags(line)
        line = replace_italic_tags(line)

        m = check_if_list_item(line)
        if m:
            unordered_list += m
            res += U_LIST.format(unordered_list) if is_last_line(i, lines) else ''
            continue
        elif not m and unordered_list:
            res += U_LIST.format(unordered_list)
            unordered_list = ''

        line = catch_all_in_p_tag(line)
        res += line
    return res
