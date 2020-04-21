# на вход подается массив и число
# вернуть пары чисел сумма которых равна этому числу
# 


def twosum(nums, target):
    lookup = {}
    pair = []
    for cnt, num in enumerate(nums):
        if target - num in lookup:
            pair.append((nums[lookup[target-num]], nums[cnt]))
        lookup[num] = cnt
    return pair
    


if __name__ == "__main__":
    digits = [4, 3, 3, 2, 1, 5, 10, 6, 15, 20, 16]
    target_sum = 7
    print(twosum(digits, target_sum))