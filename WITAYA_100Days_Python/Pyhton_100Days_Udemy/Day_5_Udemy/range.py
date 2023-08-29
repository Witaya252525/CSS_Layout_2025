


import colorama
import random

from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

for number in range (1 ,11,3):
    print(number)                                                  



total = 0
for i in range (1 ,101):
    total += i
    print(i)

print(total)
