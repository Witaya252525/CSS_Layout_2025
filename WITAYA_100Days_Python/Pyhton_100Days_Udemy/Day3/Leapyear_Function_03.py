
# Leap is the year that is 366 days
# year = input("Which year do you want to check ")
""" The leap year is 3 condition  year mod % 4 == 0 is
  leap year then year mod % with 100  !== 0 is leap year 
  leap is year % 400  == o
""" 

def leap_checking(year):
    if ((year % 400 ) == 0) or ((year%4 ==0) and (year%100 != 0)):
        return True
    
    else:
        return False
    

meta = int(input("Which year do you want to check ==>  "))
print(meta)
if leap_checking(meta) == True:
    print(f'The {meta} , is leap year') 
else:
    print(f'The {meta} , is not leap year') 
