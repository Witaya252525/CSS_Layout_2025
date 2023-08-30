
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

# Import the random module here
# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
print(names)
#Write your code below this line 👇
length = random.randint(0,len(names))
print(length)
print(f'This meal who will pay1 is {names[length-1]}  ')
print("program number#2")
print(f' This meal who will pay2 is {random.choice(names)} ')
