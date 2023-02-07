#Модули в Python
#1 Встроенные модули
import time, random
import math

print(math.pi)

from math import e as i

print(i)

#2 Собственные модули
#import Lesson3
from Lesson3 import Person
per1 = Person('name', 'last', 99, 'qwerty')
per1._s()

#3 Заимствованные модули