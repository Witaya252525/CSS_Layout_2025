import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED+Back.BLACK)



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''






#https://ascii.co.uk/art/scissors
game_images = [rock ,paper ,scissors]
user_chioce = (int(input("what is you should ==>  0 for rock  1 for paper  2 for scissors ")))
computer_choice = random.randint(0, 2)

print(f' computer  choice {computer_choice} ')
print(game_images[computer_choice])
print(game_images[user_chioce])


if user_chioce >=3 or user_chioce < 0 :
    print('You type invalid criteria , you loose')


elif user_chioce ==0 and computer_choice ==2 :
    print ("You win")

elif computer_choice ==0  and  user_chioce ==2 :
    print(" you loos ")


elif computer_choice > user_chioce :
    print(" you loos ")

elif user_chioce > computer_choice :
    print(" you loos ")    

elif user_chioce == computer_choice :
    print (" Is a Draw ")
