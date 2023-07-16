# print("welcome to the rollercoaster ")
# height = int(input("What is you height in cm ==>  ?"))
# if height >= 120 :
#     print("You can ride Roaller coaster ")

# else:
#     print("Sorry you have to grow taller before you can ride")
    
# print(" Check odd or event number  ")
# number=int(input("Please enter the number "))
# if (number % 2 ) == 0 :
#     print (f' this  = {number} is odd ')

# else:
#      print( " This number is event ")





print(" Check Height for Roaroller ")
height = int(input("Please in put height == "))
if height >= 120 :
    bill = 0 
    print(" you can right roller crosster")
    age = int(input("please in put your age ++ "))
    if age < 12 :
        bill = 8 
        print("Please pay = 8")
    elif age <=18:
        bill = 28 
        print("Please pay = 28")
    else:
        bill = 88 
        print("Please pay = 88")

    Need_Pic =(input("Do you want Photo Y or N   "))
    if Need_Pic =="Y":
        bill+= 3
        print(f"You total bill is {bill}")
    
else:
    print(" Sirry You can not ride Roller couster")
