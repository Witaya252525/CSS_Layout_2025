year = int(input("which year you want to checking => "))

if year % 4 == 0:
    if year % 100 != 0:
        print("This year is leap year")
        
    # year % 100 = 0 and ==>
    else:
        print(f'This {year} not the leap year')
        if year % 400 == 0:
            print("This year is leap year")
        else:
            print("This year is not leap year")



else:
    print(f'This {year} not the leap year')
