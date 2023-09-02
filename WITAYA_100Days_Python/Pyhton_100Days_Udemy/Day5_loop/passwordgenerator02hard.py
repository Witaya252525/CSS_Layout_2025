#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# add all the thing to list
# how to re order in list == random.shuffer 
password_list = [ ]
#what is different 0-nr or 1-nr
for cha in range ( 0 , nr_letters):
     random_cha = random.choice(letters)
     password_list += random_cha
     random.shuffle(password_list)
print(f'The random cha in list is {password_list}')


     
for sym in range ( 0 , nr_symbols):
     random_sym = random.choice(symbols)
     password_list += random_sym
print(f'The random with symbol in list is {password_list}')


for num in range ( 0 , nr_numbers):
     random_num = random.choice(numbers)
     password_list += random_num
print(f'The random password in list is {password_list}')


# if password_list = random.shuffle(password_list)   can not define type
random.shuffle(password_list)
print(password_list)


# loop for convert list into string
password = " "
for char in password_list :
     password +=char

print(f'The final password is {password}')




