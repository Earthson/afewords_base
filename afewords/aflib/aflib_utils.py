from HTMLParser import HTMLParser


def strip_tags(html, length):
    html = html.strip()
    html = html.strip("\n")
    result = []
    parser = HTMLParser()
    parser.handle_data = result.append
    parser.feed(html)
    parser.close()
    return ''.join(result)[:length]

def section_cmp(sec0, sec1):
    sec0 = [int(each) if each.isdigit() else each for each in sec0.split('.')]
    sec1 = [int(each) if each.isdigit() else each for each in sec1.split('.')]
    return cmp(sec0, sec1)


import re

_url_pattern = r'(\b(?:http|ftp|https)://(?:.*?)(?:\s|$))'
_url_rex = re.compile(_url_pattern)

def is_url(tojudge):
    ret = _url_rex.match(tojudge)
    if ret is None:
        return False
    return True

