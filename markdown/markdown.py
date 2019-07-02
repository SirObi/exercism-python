import re
from collections import OrderedDict

OPENING_TAG = '<{}>'
CLOSING_TAG= '</{}>'
U_LIST = '<ul>{}</ul>'
LIST_ITEM = '<li>{}</li>'
STRONG = '<strong>{}</strong>'
ITALIC = '<em>{}</em>'
PARAGRAPH = '<p>{}</p>'
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
            return OPENING_TAG.format(v) + rest_string + CLOSING_TAG.format(v)
    return l


def replace_bold_tags(l=''):
    line_with_bold = re.match('(.*)__(.*)__(.*)', l)
    if line_with_bold:
        return line_with_bold.group(1) + \
            STRONG.format(line_with_bold.group(2)) + line_with_bold.group(3)
    return l


def replace_italic_tags(l=''):
    line_with_ital = re.match('(.*)_(.*)_(.*)', l)
    if line_with_ital:
        return line_with_ital.group(1) + \
            ITALIC.format(line_with_ital.group(2)) + line_with_ital.group(3)
    return l


def apply_p_tag_if_no_tag(l=''):
    return l if re.match('<h|<ul|<p|<li', l) else PARAGRAPH.format(l)


def check_if_list_item(l=''):
    list_item = re.match(r'\* (.*)', l)
    if list_item:
        return LIST_ITEM.format(list_item.group(1))
    return False


def is_last_line(i, _list):
    return _list.index(i) == len(_list) - 1


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    current_list = ''
    for i in lines:
        line = replace_header_tags(i)
        line = replace_bold_tags(line)
        line = replace_italic_tags(line)

        list_item = check_if_list_item(line)
        if list_item:
            current_list += list_item
            res += U_LIST.format(current_list) if is_last_line(i, lines) else ''
        else:
            res += U_LIST.format(current_list) if current_list else ''
            current_list = ''
            res += apply_p_tag_if_no_tag(line)
    return res
