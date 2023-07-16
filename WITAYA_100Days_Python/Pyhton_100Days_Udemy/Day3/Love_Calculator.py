
print("Welcome to love Calculator")
name1 = input("What is your  name 1 \n ")
name2 = input("What is your name  2 \n ")
#TRUE LOVE
n1lower = name1.lower()
print(n1lower)
n2lower = name2.lower()
print(n2lower)
combi_name = n1lower + n2lower
print(combi_name)

score = 0
t = combi_name.count("t")
score+=t 
r = combi_name.count("r")
score+=r
u = combi_name.count("u")
score+=u
e = combi_name.count("e")
score+=e
l = combi_name.count("l")
score+=l 
o = combi_name.count("o")
score+=o
v = combi_name.count("v")
score+=v
e = combi_name.count("e")
score+=e

print(score)
print(type(score))

if (score < 10) or (score > 90):
    print(f' your love scrore is {score} ,you go to gether like coke')
elif (score >= 40) and (score <= 50):
    print(f' your love scrore is {score} ,you are alright')

else:
    print(f' your love scrore is {score} ')



