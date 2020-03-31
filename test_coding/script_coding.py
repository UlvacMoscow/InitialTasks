import re


class ServiceCoder:
    def __init__(self, input_str: str) -> None:
        self.input_str = input_str

    def check_string(self) -> str:
        raise NotImplementedError

    def coder(self) -> str:
        raise NotImplementedError


class EncodingString(ServiceCoder):

    def coder(self) -> str:
        encoding_string = ''
        step = 0
        for quantity in self.input_str[::2]:
            encoding_string += quantity * int(self.input_str[1::2][step])
            step += 1
        return encoding_string

    def check_string(self) -> str:
        if self.input_str[::2].isalpha() and self.input_str[1::2].isdigit() \
         and len(self.input_str[::2]) == len(self.input_str[1::2]):
            return self.coder()

    # def check_string(self) -> str:
    #     if re.match(r'^(\w\d+)+$', self.input_str):
    #         return self.coder()
        else:
            raise TypeError("""Строка расшифровки должны состоять из чередующийся последовательно
            букв и цифр, начинатся строго с буквы и заканчиваться цифрой (А2H3L4)""")


class CodingString(ServiceCoder):

    def coder(self) -> str:
        counter = 1
        coding_string = ''
        length_array = len(self.input_str) - 1
        step = 0
        for elem in self.input_str:
            if self.claime_out_range(step, length_array):
                coding_string += elem + str(counter)
            else:
                if elem == self.input_str[step + 1]:
                    counter += 1
                else:
                    coding_string += elem + str(counter)
                    counter = 1
                step += 1
        return coding_string

    def check_string(self):
        if self.input_str.isalpha():
            return self.coder()
        else:
            raise TypeError('Строка для кодирование должны состоять только из букв!')

    def claime_out_range(self, step: int, length_array: int) -> bool:
        return True if step == length_array else False


def fork(condition: bool, input_string: str) -> str:
    coder = CodingString(input_string) if condition else EncodingString(input_string)
    return coder.check_string()


if __name__ == "__main__":
    # str1 = 'ABAAABBBBBBCCtCGGGGRRR'
    # str2 = 'A3B2C4D1H3'
    # str3 = 'ABAAABBBBBBCCtCGGGGRRR'
    str4 = 'A1D10'
    # print(fork(True, str1))
    # print(fork(False, str2))
    # print(fork(False, str3))
    print(fork(False, str4))
    # print(fork(True, str3))