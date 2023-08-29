import colorama
import random
import mymodule

from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)


random_float = random.random()
print(random_float)


names_strsing1  = "witaya,chaison"
print(names_strsing1.split(','))


names_strsing2  = 'witaya/chaison/Nakornpranom'
print(names_strsing2.split('/'))

names_strsing3  = 'witaya ,chaison ,Nakornpranom'
print(names_strsing3.split(':'))

names_strsing3  = 'witaya ,chaison ,Nakornpranom'
print(names_strsing3.split())

names_strsing3  = 'witaya ,chaison ,Nakornpranom'
print(names_strsing3.split())