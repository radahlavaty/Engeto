HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random

random_word = random.choice(word_list)
print(f"Word to be guessed is {random_word}")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.



#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# guessed_places = []
# guessed_places_true = []

# for i in range(0,len(random_word)):
#   guessed_places.append("False")
#   guessed_places_true.append("True")
  
# wrong_guesses = 0
# while wrong_guesses < 5:
#   letter = input("Guess a letter: ").lower()
#   guess = "False"
#   for i , place in enumerate(random_word):
#     if place == letter and guessed_places[i] == "False":
#       guessed_places[i] = "True"
#       if guessed_places_true == guessed_places:
#         print("Win the game!")
#         break
#       guess = "True"
      
#   if guess == "False":
#     wrong_guesses += 1
    
#   print(guessed_places)
#   print(f"Amount of wrong guesses: {wrong_guesses}")
  
# print("You lost the game!")

guessed_places = []
guessed_places_true = []

for i in range(0,len(random_word)):
  guessed_places.append("_")

wrong_guesses = 0
while wrong_guesses < 6:
  letter = input("Guess a letter: ").lower()
  guess = "False"
  for i , place in enumerate(random_word):
    if place == letter and guessed_places[i] == "_":
      guessed_places[i] = letter
      #print(random_word)
      #print(''.join(guessed_places))
      if random_word == ''.join(guessed_places):
        print("Win the game!")
        exit()
      guess = "True"

  if guess == "False":
    wrong_guesses += 1

  print(guessed_places)
  print(f"Amount of wrong guesses: {wrong_guesses}")
  print(HANGMANPICS[wrong_guesses])

print("You lost the game!")
print(HANGMANPICS[-1])