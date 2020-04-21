

def sort_list(input_list):
    for index, elem in enumerate(input_list):
        temp_value = elem
        temp_index = index
        while temp_index > 0 and (input_list[temp_index - 1] > temp_value):
            input_list[temp_index], input_list[temp_index - 1] = input_list[temp_index - 1], input_list[temp_index]
            temp_index -= 1
    return input_list



if __name__ == "__main__":
    digits_list = [40, 11, 34, 3,3, 45, 76,77,90, 77, 89]
    print(sort_list(digits_list))