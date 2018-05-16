def binary_search(digist_list, target, begin, finish):
    if begin > finish:
        return False
    else:
        middle = (begin + finish) // 2
        if target == digist_list[middle]:
            return  middle
        elif target < digist_list[middle]:
            return binary_search(digist_list, target, begin, finish -1)
        else:
            return binary_search(digist_list, target, begin + 1, finish)


digist_list = [2, 13, 23, 35, 43, 47, 48, 51, 66, 68, 74, 88, 91, 95, 100]
target = 47
begin = 0
finish = len(digist_list)

coincidence = binary_search(digist_list, target, begin, finish)

if coincidence == False:
    print('Item', target, 'Not Found!')
else:
    print('Item', target, 'Found at Index', coincidence)