import colorama

from Lesson6 import *

print(colorama.Fore.BLUE)


class MegaHuman(SuperHuman):
    def __str__(self):
        return f'{self.name} {self.age} {self.wings} '


hum3 = MegaHuman('ислам', 18)
hum3.flying()


# print(hum3.fly())


class Bank:
    def __init__(self, name, age, balance, key: str):
        self.name = name
        self.age = age
        self._money = balance
        self.__k = key

    def set_key(self):
        if len(self.__k) >= 8:
            return self.__k
        else:
            raise ValueError(f'длина меньше 8см)')

    def __str__(self):
        return f'{self.name} {self._money}'


bank = Bank('Асылбек', 16, 4000, 'qwertythgerfd')
# print(bank)
bank.set_key()
print(dir(Bank))
print(bank._Bank__k)
bank._Bank__k = 123231242231
print(bank._Bank__k)