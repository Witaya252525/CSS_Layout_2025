import colorama
import random

from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

sum = 0
for i in range (1,100):
    if  i % 2 ==0 :
        sum+=i
print(sum)   
        
                                                  