
def page_split(objs, curpage, num_each = 10):
    st = num_each * (curpage - 1)
    ed = st + num_each
    page_list = [i/num_each + 1 for i in range(0, len(objs), num_each)]
    return objs[st:ed], page_list
