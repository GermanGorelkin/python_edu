def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 != 0:
            del l[i]
        else:
            l[i] = l[i] // 2
            i += 1
