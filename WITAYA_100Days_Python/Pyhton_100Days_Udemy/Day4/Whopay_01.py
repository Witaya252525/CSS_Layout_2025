import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

import random

# random_integer = random.randint(1,100)
# print(random_integer)

# random_float  = random.random()
# print(random_float)


# random_float  = random.random()*5
# print(random_float)
# how to do if name is very
names_string = input ("Give me everybody's name , separate by comma  ")
print(names_string)
name = names_string.split(",")
print(name)
print(f' The name who will pay is {name[random.randint(0,1)]} ')