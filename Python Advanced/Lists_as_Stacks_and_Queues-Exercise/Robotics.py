def timing(h, m, s):
    s += 1
    if s == 59:
        s = 0
        m += 1
    if m == 59:
        m = 0
        h += 1
    if h == 23:
        hours = 0
    return h, m, s
