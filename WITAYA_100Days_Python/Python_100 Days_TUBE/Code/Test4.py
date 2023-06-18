
def print_multiplication_table(n):
    for i in range(1,11):
        for j in range(1,1+n):
            print(i*j , end ="\t")
        print()

mul=int(input("Please Enter the number : "))  
print_multiplication_table(mul)

