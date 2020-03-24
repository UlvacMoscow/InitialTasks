class EncodingString:

    def fork(self, condition, input_string):
        return self.check_string_coding(input_string) if condition  \
            else self.check_string_encoding(input_string)

    def check_string_coding(self, input_string):
        if input_string.isalpha():
            return self.function_coding(input_string)
        else:
            raise TypeError('Строка для кодирование должны состоять только из букв!')

    def check_string_encoding(self, input_string):
        if input_string[::2].isalpha and input_string[::2].isdigit \
            and len(input_string[::2]) == len(input_string[1::2]):
            return self.function_encoding(input_string)
        else:
            raise TypeError("""Строка расшифровки должны состоять из чередующийся последовательно  
            букв и цифр, начинатся строго с буквы и заканчиваться цифрой (А2H3L4)""")
             

    def function_coding(self, input_string: str) -> str:
        counter = 1
        coding_string = ''
        length_array = len(input_string) - 1
        step = 0
        for elem in input_string:
            if self.control_out_range(step, length_array):
                coding_string += elem + str(counter)
            else:
                if elem == input_string[step + 1]:
                    counter += 1
                else:
                    coding_string += elem + str(counter)
                    counter = 1
                step += 1
        return coding_string

    def control_out_range(self, step: int, length_array: int) -> bool:
        return True if step == length_array else False

    def function_encoding(self, input_string: str) -> str:
        encoding_string = ''
        step = 0
        for elem in input_string[::2]:
            encoding_string += elem * int(input_string[1::2][step])
            step += 1
        return encoding_string


str1 = 'ABAAABBBBBBCCtCGGGGRRR'
str2 = 'A3B2C4D1H3'
str3 = 'AB1AAABBBBBBCCtCGGGGRRR'


test = EncodingString()
print(test.fork(True, str1))
print(test.fork(False, str2))
print(test.fork(False, str3))
print(test.fork(True, str3))


