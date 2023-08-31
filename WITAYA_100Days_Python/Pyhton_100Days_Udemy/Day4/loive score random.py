import colorama
import random
import mymodule

from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)


# while True:
#    # import random
#    random_integer  = random.randint(1,10)

#    print(random_integer)
#    if random_integer == 9:
#           print("I Love YOU")
#           break
    
# print(mymodule)                    
# print(mymodule.pi)  



# random_float =random.random()
# print(random_float*9)

while True:
  love_score = random.randint(1,20)
  if love_score >= 5: 
     print(f' you love score is  ==> {love_score}')
     if love_score == 7: 
        break
  

   