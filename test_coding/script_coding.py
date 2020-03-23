#  «Необходимо реализовать алгоритм кодирования/декодирования длин серий — алгоритм сжатия данных, 
#  заменяющий повторяющиеся символы на один символ и число его повторов. 

# Серией называется последовательность, состоящая из нескольких одинаковых символов (более одного). При 
# кодировании строка одинаковых символов, составляющих серию, заменяется строкой, содержащей сам 
# повторяющийся символ и количество его повторов.

# Например, строка AAAABBB будет сжата в строку A4B3, а строка AAAAAAAAAAAAAAABAAAAA — в строку A15BA5.


# Нужно на python реализовать две функции, кодирующую и декодирующую строки. Написать программу, 
# использующую данные функции. В качестве параметров программы должен быть параметр определяющий, 
# компрессируем или декомпрессируем и имена одного входного и одного выходного файлов.» 



str1 = 'ABAAABBBBBBCCtCGGGGRRR'

def function_coding(input_string: str) -> str:
    counter = 1
    coding_string = ''
    length_array = len(input_string) - 1
    step = 0
    for elem in input_string:
        if control_out_range(step, length_array):
            coding_string += elem + str(counter)
        else:
            if elem == input_string[step + 1]:
                counter += 1
            else:
                coding_string += elem + str(counter)
                counter = 1
            step += 1
    return coding_string


def control_out_range(step: int, length_array: int) -> bool:
    return True if step == length_array else False

print(function_coding(str1))

str2 = 'A3B2C4D1H3'


def function_encoding(input_string: str) -> str:
    encoding_string = ''
    step = 0
    for elem in input_string[::2]:
        encoding_string += elem * int(input_string[1::2][step])
        step += 1
    return encoding_string

print(function_encoding(str2))


