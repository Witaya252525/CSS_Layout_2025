


witaya = True
while witaya:


      print("Which character are you from 'Avengers?'")
      print()
      print("Answer these questions and let's find out.")
      print()
      print("Please use Y or N for yes and no.")
      
      likeGreen = input("Do you like the color green?: ")
      if likeGreen.lower() == "y":
            print("You must be the Hulk!")
      
      IronIsCool = input("Do you think building robots is cool?: ")  
      if IronIsCool.lower() == "y":
            print("You must be Iron Man. Cool suit!")
      
      TimeTravel = input("Do you like traveling through time?: ")  
      if TimeTravel.lower() == "y":
            print("You must be Captain America!")
      
      Strong = input("Are you super strong?: ")
      if Strong.lower() == "y":
            print("You have got to be Thor!")
      else:
            print("I guess you are not like anyone from 'Avengers.'")
            witaya = False
      
