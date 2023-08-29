


import colorama
import random

from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)


for i in range (1 ,102,1):
    if i%3 == 0:
        print("Fiz")
    elif i%5 == 0:
        print("Buzz"

    elif (i%5 == 0) and (i%3 == 0) :
        print("FizBuzz") 

    else:
        print(i)








