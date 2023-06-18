


def print_multiplecation_table(n):
    for i in range(1,11):
        for j in range(1,n+1):
            print(i*j, end ='\t')
        print()
mul = int(input("Please  Enter your Number: "))
print_multiplecation_table(mul)