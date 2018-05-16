"""

sum = 0 + 1 + 2 + 3 + 4 + 5 ....

"""


def sum_of_the_sequence(x):
    if x == 0:
        return 0
    else:
        return x + sum_of_the_sequence(x - 1)


print(sum_of_the_sequence(1))