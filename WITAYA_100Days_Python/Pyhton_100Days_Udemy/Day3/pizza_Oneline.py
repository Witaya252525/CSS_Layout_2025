import colorama
from colorama import Fore ,Back ,Style
colorama.init()
print(Fore.RED+Back.BLACK)



print("Welcome to Python pizza delivery ")
size = input("Please in put S M L  ")
# add_pepperoni = input(" Do you want pepperoni Y  N  ")
# extra_cheese  = input(" Do you want extra cheese Y N  ")

bill = 0
# outcome =  (bill := 15) if size == "S" else (bill := 25) if size == "M" else (bill := 85 )
(bill := 15) if size == "S" else (bill := 25) if size == "M" else (bill := 85 )
# print(bill)
add_pepperoni = input("Do you want pepperoni Y  N  ")
# if add_pepperoni =='Y' :outcome+=2 
se =input("What size you need  S M  ") if add_pepperoni =='Y' else ("") if add_pepperoni =='N' else ("")
# if add_pepperoni =='Y': se =input("What size you need  S M  ")
(bill2:=3) if se == "M" else (bill2:=2) if se == "S" else (bill2:=0)
bill+=bill2
# print(f'{bill}')
# bill +=2 if size =='M' else bill+3 if size == "S"
extra_cheese  = input("Do you want extra cheese Y N  ")
# if extra_cheese =='Y' :print(f'Your total pay ment is ==> {bill+1}')
print(f'Your total pay ment is ==> {bill+1}') if extra_cheese =='Y' else print(f'Your total pay ment is ==> {bill}') if extra_cheese =='N' else ("")