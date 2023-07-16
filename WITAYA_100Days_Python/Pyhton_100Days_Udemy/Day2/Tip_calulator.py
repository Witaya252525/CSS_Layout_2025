
# "{ :0.2f}".format(bills}  
import colorama
from colorama import Fore ,Back ,Style
colorama.init()
print(Fore.RED+Back.BLACK)

bills =  float(input('what is total bill $ '))
man  =   int(input('what is total friends come with ::  '))
tip =    float(input('what is % tip%   ')) *0.01 * bills
print(" tip amount is  = " ,tip)
print(" Total billls is $ = " , (tip+bills))

print(f' you bills per people  is $  {(bills +tip)/(man) :0.2f}  ' ) 

