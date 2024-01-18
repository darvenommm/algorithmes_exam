MAXLEN = 100
SYS = 10

def add(a, st_a, b, st_b):
    res = [0 for i in range(MAXLEN)]
    flag = 0
    mxop = a if st_a > st_b else b
    mnop = a if st_a <= st_b else b
    st_min = min(st_a, st_b)
    st_max = max(st_a, st_b)
    st = st_min

    for i in range(MAXLEN-1, st_max - 1, -1):
        res[i] = mxop[i] + mnop[i] + flag
        flag = res[i] // SYS
        res[i] %= SYS

    for i in range(st_max - 1, st_min - 1, -1):
        res[i] = mnop[i] + flag
        flag = res[i] // SYS
        res[i] %= SYS

    if flag:
        res[st-1] = flag
    return res, st
