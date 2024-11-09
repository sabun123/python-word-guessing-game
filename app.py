# 9 November 2024 Yusuf Ismail Shukor

import random
from app.greet import greet_player

# Display all of the unguessed letters as underscores
# i.e: ________

greet_player()

words = ['python', 'engineer', 'programmer', 'developer', 'list', 'tuple', 'dictionary']
selected_word = random.choice(words)

incorrect_guesses_left = len(selected_word)
# strings are immutable in Python, so we will store this as a list
guessed_spaces = list('_' * len(selected_word))

while incorrect_guesses_left > 0 and '_' in guessed_spaces:
  # we don't want to print a list,  just a string so we convert it to a string
  print(''.join(guessed_spaces))
  print("Incorrect guesses left: " + str(incorrect_guesses_left))
  print('')
  guess = input('Enter your guessed letter: ')

  if guess in selected_word:
    print('Correct guess!')
    for index, letter in enumerate(selected_word):
      if letter == guess:
        guessed_spaces[index] = letter
  else:
    print('Uh-oh! That ain\'t it!')
    incorrect_guesses_left -= 1

if('_' not in guessed_spaces):
  print('You won!')
else:
  print('You lost!')

print('GAME OVER')
print('')