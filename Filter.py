#  filter (func, iterable)


def check_o(string):
    return 'o' in string.lower()


lst = ['global', 'local', 'place', '34343', 'oooo']

new_lst = list(filter(check_o, lst))

print(new_lst)

new_lst_2 = list(filter(lambda string: 'o' in string.lower(), lst))

print(new_lst_2)

new_lst_3 = [string for string in lst if check_o(string)]

print(new_lst_3)
