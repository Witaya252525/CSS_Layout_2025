


import colorama
import random

from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

#becareful the order of the program because just onconditons is true.
for i in range (1 ,102,1):

    if (i%5 == 0) and (i%3 == 0) :
        print("1FizBuzz") 
    
    elif i%3 == 0:
        print("2Fiz")

    elif i%5 == 0:
        print("3Buzz")


    else:
        print(f'condition 4 is= {i}')








