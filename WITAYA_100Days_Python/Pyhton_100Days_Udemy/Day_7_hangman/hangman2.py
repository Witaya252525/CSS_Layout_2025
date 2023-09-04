

import random

word_list = [ "ardvardk","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
print(list(chosen_word))

display = [ ]   # for letter in chosen_word: display += "_"
for _ in range (len(chosen_word)):
    display += "_"
    print(display)

guess = input("Guess the a letter: ").lower()
for position in range (len(chosen_word)) :
    if   guess == chosen_word[position]:
         display[position] = guess 
     
    else:
         print("wrong")                                                                                                       
print(display)