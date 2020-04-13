from collections.abc import Iterable


a = [1,4,5,7]
b = 3
c =[3,[43,4]]



def wrapper(*args):
    temp = []
    for x in args:
        if isinstance(x, Iterable):
            temp += wrapper(*x)
        else:
            temp.append(x)
    return temp


print(wrapper(a,b,c))
