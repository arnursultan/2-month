import colorama

# print(colorama.Back.RED)
# print(colorama.Back.BLACK)


# mro порядок разрешения методов

class Human:
    head = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age


hum = Human('beka', 19)
hum.name = 'beks'


class SuperHuman(Human):
    def __init__(self, name, age, wings=False):
        super().__init__(name, age)
        self.wings = wings

    def flying(self):
        self.wings = True
        return f'{self.name} in Fly'

    def fly(self):
        if self.wings != False:
            return self.flying()
        else:
            return 'not Flying'


hum2 = SuperHuman('Николай', 20)
hum2.flying()
# print(hum2.fly())