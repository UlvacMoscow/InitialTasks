before_sort_list = [78, 45, 55, 11, -5, 9]


def bubble_sort(my_list):
    last_item = len(my_list) - 1
    for z in range(0, last_item):
        for x in range(0, last_item - z):
            print(my_list)
            if my_list[x] > my_list[x + 1]:
                my_list[x], my_list[x + 1] = my_list[x + 1], my_list[x]
    return my_list


print('before sort list', before_sort_list)
after_sort_list = bubble_sort(before_sort_list)
print('after sort list', after_sort_list)