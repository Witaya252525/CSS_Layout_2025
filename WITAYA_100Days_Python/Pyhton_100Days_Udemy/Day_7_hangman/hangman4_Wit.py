

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["ardvardk", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
print(list(chosen_word))

display = []   # for letter in chosen_word: display += "_"
for _ in range(len(chosen_word)):
    display += "_"
    print(display)



end_of_game = False
lives = 6
while not end_of_game:

    guess = input("Guess the a letter: ").lower()
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess

        else:
            print("not match")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = False
            print("you loose")
    print(stages[lives])