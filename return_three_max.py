lst = [141, -200, 2000, 1, 17, -7, -17, -27, 18, 541, 8, 10001, 7, 7]

def three_max_els(lst: list):
    max_three = [None, None, None]
    for el in lst:
        # first iter
        if max_three[2] is None:
            max_three[2] = el
            continue
        # second iter
        if max_three[1] is None:
            if el > max_three[2]:
                max_three[1], max_three[2] = max_three[2], el
            else:
                max_three[1] = el
            continue
        #third iter
        if max_three[0] is None:
            if el > max_three[2] and el > max_three[1]:
                max_three[0], max_three[1], max_three[2] = max_three[1], max_three[2], el
            elif el > max_three[1] and el < max_three[2]:
                max_three[0], max_three[1] = max_three[1], el
            else:
                max_three[0] = el
            continue

        if el > max_three[2] and el > max_three[1]:
            max_three[0], max_three[1], max_three[2] = max_three[1], max_three[2], el
        elif el > max_three[1] and el < max_three[2]:
            max_three[0], max_three[1] = max_three[1], el
        elif el > max_three[0] and el < max_three[1]:
            max_three[0] = el
    return max_three



if __name__ == "__main__":
    print(three_max_els(lst))