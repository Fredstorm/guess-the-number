#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(r"""
  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                              
""")

lives = input("Easy mode or hard mode? (answer with 'easy' or 'hard') ")
if lives == "easy":
  lives = 10
elif lives == "hard":
  lives = 5
else:
  print("Invalid response run the program again.")

import random
import sys

correct_number = random.randint(1,100)

win = False

while lives > 0:
  guess = int(input("Guess a number from 1 to 100. "))
  if guess > correct_number:
    print("Too high.")
    lives -= 1
    print(f"{lives} guesses left.")
  elif guess < correct_number:
    print("Too low.")
    lives -= 1
    print(f"{lives} guesses left.")
  else:
    print(f"Congratulations you guessed the number {correct_number} with {lives} guesses left!")
    win = True
    lives = 0

if lives == 0:
  if win == False:
    print(f"You ran out of guesses. The number was {correct_number}.")
    sys.exit("Game Over.")
    
  elif win == True:
    sys.exit("Game Over")
  
    





