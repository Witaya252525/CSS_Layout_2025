import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

while True:

   row1= ["" ," " ," "]
   row2= ["" ," " ," "]
   row3= ["" ," " ," "]
   map = [row1 ,row2 ,row3]
   print(f' {row1}\n {row2}\n {row3}\n')
   posittion =input("where do you want to go ==> ")

   # 23 is index position  (0 is first and 1 is second position)
   horizontal = int(posittion[0])
   vertical = int(posittion[1])

   
   map[vertical-1][horizontal-1] = "80"
   print(f' {row1}\n {row2}\n {row3}\n')

   