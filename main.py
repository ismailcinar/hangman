

import random
from turtle import clear

stages =['''
  +---+
  |   |       
  0   |
 /|\  |
 /  \ |
      |
 =======
 ''','''
 +---+
  |   |       
  0   |
 /|\  |
 /    |
      |
 =======
 ''','''
 +---+
  |   |       
  0   |
 /|\  |
      |
      |
 =======
 ''','''
 +---+
  |   |       
  0   |
 /|   |
      |
      |
 =======
 ''','''
 +---+
  |   |       
  0   |
  |   |
      |
      |
 =======
 ''','''
 +---+
  |   |       
  0   |
      |
      |
      |
 =======
 ''','''
 +---+
  |   |       
      |
      |
      |
      |
       ''']
word_list=["araba","bisiklet","tekerlek"]
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
lives = 6
#print(f'Psst, the solution is {chosen_word}.')

display=[]
for _ in chosen_word:
  display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("guess a letter:  ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
         display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose.")

   # print(display)
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game =True
        print("you win")

    print(stages[lives])