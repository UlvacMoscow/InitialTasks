default = [1, 2]


def add_list(lis, a):
    lis.append(a)
    return lis


default = add_list(default, 5)
print(default)
default = add_list(default, 5)
print(default)
default = add_list(default, 5)
print(default)
