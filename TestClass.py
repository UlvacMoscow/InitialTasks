
class Man:
    def __init__(self):
        self.__age = None
        self.__name = None

    def set_name(self, name):
        self.__name = name

    def set_age (self, age):
        self.__age = age

    def info(self):
        print(self.__age, self.__name)


m = Man()
m.set_age(22)
m.set_name('ivan')
m.info()
