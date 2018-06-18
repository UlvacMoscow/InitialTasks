b = [1, 3]
c = [5]


def upd(a):
    return b.append(a)


upd(c)
upd(c)
print(type(b))
