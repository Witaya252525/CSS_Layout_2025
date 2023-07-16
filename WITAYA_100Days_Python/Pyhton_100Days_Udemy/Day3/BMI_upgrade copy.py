

print("This code design for Checking BMI")
height = float(input("Enter your height in m  "))
weight = float(input("Enter your wight in kg  "))
# add  round number 0.2f
BMI = ((weight)/(height*height))
print(f"{BMI:0.2f}")

if BMI <= 18.5:
    print(f" you BMI is {BMI}  now is under wight")

elif BMI > 18.5 and BMI <= 25:
    print(f" you BMI is {BMI}  now is Normal")

elif BMI > 25 and BMI <= 30:
    print(f" you BMI is {BMI}  now is over weight")

elif BMI > 30 and BMI <= 35:
    print(f" you BMI is {BMI}  now is obese")

elif BMI > 35 :
    print(f" you BMI is {BMI}  now is Clinucally obese")
