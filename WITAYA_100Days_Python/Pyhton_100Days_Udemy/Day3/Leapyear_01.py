
# "{ :0.2f}".format(bills}
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)


year = int(input('Enter year to checking ==> '))

if year % 4 == 0:
    if year % 100 == 0: # divided by 100 must not remian 00
        if year % 400 == 0:



            print(f' this year {year} = is leap year')

        else:
            print(f' this year {year} = not ! leap year')

    else:
        print(f' this year {year} = leap year')

else:

    print(f' this year {year} = not ! leap year')
