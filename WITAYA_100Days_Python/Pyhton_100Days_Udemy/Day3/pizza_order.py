print("Welcome to Python pizza delivery ")
size = input("Please in put S M L  ")
add_pepperoni = input(" Do you want pepperoni Y  N  ")
extra_cheese  = input(" Do you want extra cheese Y N  ")
bill = 0
if size == "S" :
    bill = 15 
    print(" Small Pizza : $15")
    if add_pepperoni == ("Y" or 'y') :
         bill+=2
   
elif size ==  ("M" or "m" ):
    bill = 25 
    print(" Medium  Pizza : $25")
    if add_pepperoni == ("Y" or "y") :
         bill+=2
        
else:
     bill = 88 
     print("Bigger Piza  = 88")
     if add_pepperoni == ("Y" or "y") :
          bill+=2

if extra_cheese =="Y":
     bill += 1   

print("The totaly bill is  = " + str(bill)) 