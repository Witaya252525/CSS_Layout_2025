


print("Welcome to the Tresure Lsland")
print("Your mission is to find thr tresure")
cross_road = input("you are in the cross road Y N   ")
if cross_road == "left" or cross_road == "Left" :
    print("You is move on")
    water = input("you are Swing or Wait  Y N   ")
    if water ==  "wait" or water == "Wait" :
        print("You still servive")
    else:
         print(" Game Over ")   

    door = input("Pleade pick door do you like RED Blue  Yellow  ")
    if door ==  "Yellow" or door == "yellow" :
            print("You Are super win")
    else:
             print(" Game Over ")        

else:
     print(" Game Over ")

