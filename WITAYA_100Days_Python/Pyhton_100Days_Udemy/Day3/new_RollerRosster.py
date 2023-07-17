import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

print("Welcome to Rollercoaster")
height = int(input("what is you height in cm:: ? "))
if height >= 120:
    print("You can ride the  Rollercoaster 😍😘")

    age = int(input("What ia you age "))
    if age < 12:
        print(f' Child ticket are  $5')
    elif age <=18:
        print(f' Child ticket are  $7')
    else:
        print(f' Adult ticket is  $12')
else:
    print("You can play Rollenot rcoaster 😢😢")
