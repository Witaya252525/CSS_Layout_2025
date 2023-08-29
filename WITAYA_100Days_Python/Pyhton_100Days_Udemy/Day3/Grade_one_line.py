import colorama
from colorama import Fore ,Back ,Style
colorama.init()
print(Fore.RED+Back.BLACK)

# a = 100
# b = 200
# print("Greater ") if a > b else print("witaya") if a == b else print("Hero")  
#print (statement ) and (T if statement true ) or (F: if statement Fail) )

def gradeV2(score):
    return (print(( score < 0 or score > 100) and "error"  or "FFFFFDCBAAAA"[score//10]))

while True:   
    wita=int(input("Please input score == "))
    (gradeV2(wita))