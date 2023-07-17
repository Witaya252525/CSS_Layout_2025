import colorama
from colorama import Fore ,Back ,Style
colorama.init()
print(Fore.RED+Back.BLACK)

print("welcome to love calculayor")
name1 = input('what is you name 1  \n').lower()
name2 = input('what is you name 2  \n').lower()
name3 = name1+name2
di1=(name3.count('t'))+(name3.count('r'))+(name3.count('u'))+(name3.count('e'))
di2=(name3.count('l'))+(name3.count('o'))+(name3.count('v'))+(name3.count('e'))
print((str(di1)+str(di2)))
love_score = (int(str(di1)+str(di2)))

print("coke and beer ") if ((love_score <10) or (love_score > 90)) else print("good job") if 40 <=love_score <=50 else print("your are awesome")