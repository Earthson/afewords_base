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
    sec0 = sec0.split('.')
    sec1 = sec1.split('.')
    sec0 = [int(each) if each.isdigit() else each for each in sec0]
    sec1 = [int(each) if each.isdigit() else each for each in sec1]
    return cmp(sec0, sec1)
