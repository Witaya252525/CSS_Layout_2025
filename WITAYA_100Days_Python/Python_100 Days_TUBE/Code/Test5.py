def get_single_digit(number):
    if len(number) ==1 and number.isdigit():
        return True
    else:
        return False
    
while True:
    input_number = input("Please Enter a number=  ")
    if get_single_digit(input_number):
        print("Valid ingle digit")
        break
    else:
        print("Not a valid Sigle digit , Try again")



print("Single digit you enter is",input_number)
