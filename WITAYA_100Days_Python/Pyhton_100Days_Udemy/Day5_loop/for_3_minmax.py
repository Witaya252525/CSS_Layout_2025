import colorama
import random

from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

# student_scores = input("Input a list of student scores ").split()
# scores = 0
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#   scores +=student_scores[n]
# print(scores)


student_scores = input("Input a list of student scores ").split()
#.sprit will convert to list


#convert string into integer
for n in range(0, len(student_scores)):
  print(student_scores[n])
  student_scores[n] = int(student_scores[n])
  print(student_scores)

max = student_scores[0]
for score in student_scores :
    if score > max :
        max = score

    else:
        max = student_scores[0]    
print(max)   


min = student_scores[0]
for score in student_scores :
    if score < min :
        min = score

    else:
        min = student_scores[0]    
print(min)    
            