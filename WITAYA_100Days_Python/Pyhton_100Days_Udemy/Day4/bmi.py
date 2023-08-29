
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)

# height = float(input("what is you height "))
# weight = float(input("what is you weight "))
# bmi = (weight/(height*height))
bmi = 34
print(bmi)

if bmi < 18.5:
    print(f' you BMI is{bmi} is underweight')
elif 18.5 <= bmi < 25:
    print(f' you BMI is{bmi} is normalweight')
elif 25 <= bmi < 30:
    print(f' you BMI is{bmi} is overweight')
elif 30 <= bmi < 35:
    print(f' you BMI is{bmi} is obese')
else:
    print(f' you BMI is{bmi} is clinical obese')
