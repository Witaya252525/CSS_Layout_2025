



import random
names_string = input("Give me everybody's names, separated by a comma. ")
names1 = names_string.split(", ")
names2 = names_string.split(' ')
# 🚨 Don't change the code above 👆
print(names1)
print(names2)


#Write your code below this line 👇
length = random.randint(0,len(names1)-1)
print(f'This meal who will pay is {names1[length]}')
