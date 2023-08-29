import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

age = 19
print(" go home" if age < 16 else "witaya" if 16 <=
      age < 18 else " SEGATE THAILAND")

# def gradeV2(score):
#     return (print(( score < 0 or score > 100) and "error"  or "FFFFFDCBAAAA"[score//10]))

def gradeV2(score):
    return print(" The is error " if (score < 0 or score > 100) else "FFFFFDCBAAAA"[score//10])

while True:
    wita = int(input("Please input score == "))
    (gradeV2(wita))
