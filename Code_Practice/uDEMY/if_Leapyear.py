year = int(input("which year you want to checking => "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This year is leap year")
        else:
            print(f'This {year} not the leap year')

    else:
        print(f'This {year} not the leap year')


else:
    print(f'This {year} not the leap year')
