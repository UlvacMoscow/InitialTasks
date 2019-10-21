
class Man:
    def __init__(self, age, name):
        self.__age = age
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def info(self):
        print(self.__age, self.__name)

    def __str__(self):
        return self.__name + " " + str(self.__age)


class Developer(Man):
    def __init__(self):
        super()
        self.__lang = None

    def set_lang(self, lang):
        self.__lang = lang

    def get_lang(self):
        return self.__lang

    def __str__(self):
        return super().__str__() + ' ' + self.__lang


d = Developer()
d.set_name('Igor')
d.set_age(34)
d.set_lang("Java")
print(d)
m2 = Man(22, 'Sasha')
print(m2)



