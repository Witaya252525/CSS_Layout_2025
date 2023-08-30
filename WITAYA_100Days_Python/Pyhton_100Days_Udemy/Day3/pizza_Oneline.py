import colorama
from colorama import Fore ,Back ,Style
colorama.init()
print(Fore.RED+Back.BLACK)


print("Welcome to Python pizza delivery ")
size = input("Please in put S M L  ")
# add_pepperoni = input(" Do you want pepperoni Y  N  ")M
# extra_cheese  = input(" Do you want extra cheese Y N  ")
bill = 0
# outcome =  (bill := 15) if size == "S" else (bill := 25) if size == "M" else (bill := 85 )
(bill := 15) if size == "S" else (bill := 25) if size == "M" else (bill := 85 )
print(bill)
# add_pepperoni = input("Do you want pepperoni Y  N  ")
# if add_pepperoni =='Y' :outcome+=2 
# se =input("Add_pepperoni or not  ") 
# # if add_pepperoni =='Y' else ("") if add_pepperoni =='N' else ("")
# # if add_pepperoni =='Y': se =input("What size you need  S M  ")
# (f'bill = bill+3) if se == "M" else (bill+=2) if se == "S" else (bill+=0)')
bill2 = 0
peporoni  = input(" Do you want peporoni  S M N  ")
# print(f'Your now pay ment is ==> {bill+3}') if peporoni =='Y' else print(f'Your now pay ment is ==> {bill+2}')
bill2 +=3 if peporoni =='M' else  bill2+2 if peporoni =='S' else  bill2+0 
print(bill2+bill) 
# bill +=2 if size =='M' else bill+3 if size == "S"
extra_cheese  = input("Do you want extra cheese Y  N  ")
# if extra_cheese =='Y' :print(f'Your total pay ment is ==> {bill+1}')
print(f'Your total pay ment is ==> {bill+1+bill2}') if extra_cheese =='Y' else print(f'Your total pay ment is ==> {bill+bill2}') if extra_cheese =='N' else ("")