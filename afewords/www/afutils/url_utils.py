
def url_with_para(baseurl, paradoc=None):
    if paradoc:
        return baseurl + '?' + '&'.join(str(ek)+'='+str(ev)
                        for ek, ev in paradoc.items())
    return baseurl
