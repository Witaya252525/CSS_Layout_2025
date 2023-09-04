# == is comparison
# print()   = emply

print("Which charecter are you from 'Advenger?'  ")
print()
print("Answer this question and let's find out")
print()
print("print Y or No for yes or no ")


likeGreen = input("Do you like the color green?: ")
if likeGreen.lower() == "y":
  print("You must be the Hulk!")
else:
  print("Im aneane")

IronIsCool = input("Do you think building robots is cool?: ")  
if IronIsCool.lower() == "y":
  print("You must be Iron Man. Cool suit!")
else:
  print("Im batCat")

TimeTravel = input("Do you like traveling through time?: ")  
if TimeTravel.lower() == "y":
  print("You must be Captain America!")
else:
  print("Im Tureman")
  

Strong = input("Are you super strong?: ")
if Strong.lower() == "y":
  print("You have got to be Thor!")
else:
  print("I guess you are not like anyone from 'Avengers.'")
