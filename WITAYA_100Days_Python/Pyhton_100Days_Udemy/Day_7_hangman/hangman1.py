

import random

word_list = [ "ardvardk","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
print(list(chosen_word))

display = [ ]   # for letter in chosen_word: display += "_"
for i in  chosen_word:
    display.append("_")
    print(display)

guess = input("Guess the a letter: ").lower()
for char in chosen_word :
    if   char == guess:
         display.append(char)
 
    else:
         print("wrong")                                                                                                       
print(display)