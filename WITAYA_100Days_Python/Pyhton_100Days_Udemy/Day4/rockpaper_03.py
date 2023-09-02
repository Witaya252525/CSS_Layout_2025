import random
import colorama


while  True:

    from colorama import Fore, Back, Style
    colorama.init()
    print(Fore.RED+Back.BLACK)



    rock = '''
    _______
    ---'  ____)
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
    ---'  ____ ____)
             ______ )
           __________)
        (____)
    ---.__(___)
    '''






#https://ascii.co.uk/art/scissors



    game_images = [rock ,paper ,scissors]
    user_chioce = (int(input("what is you should ==>  0 for rock  1 for paper  2 for scissors ")))
    computer_choice = random.randint(0, 2)
    print(type(computer_choice))

    

    if user_chioce >=3 or user_chioce < 0 :
        print('You type invalid criteria , you loose')

        ask =input("do you want to play again or not Y or N  \n")
        if ask.lower() == "n":
            break 



    else:

        print(f' computer  choice {computer_choice} ')
        print(game_images[computer_choice])
        print(game_images[user_chioce])

    if user_chioce == computer_choice :
            print('You and Computer are draw')


    elif user_chioce == 0:
            if computer_choice == 2 :
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")


    elif  user_chioce == 1:
            if computer_choice == 0:
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        
    elif user_chioce == 2:
            if computer_choice == 1:
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")


    ask =input("do you want to play again or not Y or N  \n")
    if ask.lower() == "n":
            break 

