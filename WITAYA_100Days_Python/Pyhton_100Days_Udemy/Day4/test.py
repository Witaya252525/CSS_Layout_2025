import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

import random

random_integer = random.randint(1,100)
print(random_integer)


random_float  = random.random()
print(random_float)



random_float  = random.random()*5
print(random_float)