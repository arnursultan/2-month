#Множественное наследование

class Учитель:
    def учить(self):
        print('Я умею учить')
class Строитель:
    def строить(self):
        print('Я умею строить')
class Ученик(Учитель, Строитель):...

c = Ученик
c.учить()
c.строить()

class A:
    def a(self = 1):
        print('A')
class B:
    def a(self = 1):
        print('B')
class C:
    def a(self = 1):
        print('C')

a = C
a.a()
print(C.__mro__)














