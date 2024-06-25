def right_rotation(n, ip):
    l = list(ip)
    a = []
    start = (len(l) - 1)
    stop = (len(l) - 1) - n
    step = -1
    for i in range(start, stop, step):
        b = l.pop(i)
        a.append(b)
    a.extend(l)
    st = "".join(a)
    print(st)


s = "software"
number_of_iter = 2
right_rotation(number_of_iter, s)
