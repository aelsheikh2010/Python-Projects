#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random
print(logo)

# Allow the player to submit a guess for a number between 1 and 100.

EASY_LEVEL = 10
HARD_LEVEL = 5
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def check_answer(answer,guess,turns):
  """check guess againest true answer and return number of turns"""
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")
# create function that check the difficulty level and return number of attempts
def check_difficulty():
  DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if DIFFICULTY == "easy":
    return EASY_LEVEL
  elif DIFFICULTY == "hard":
    return HARD_LEVEL
def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1,100)
  print(f"Pssst, the correct answer is {answer}")
  turns = check_difficulty()
  
  #repeate if the answer is wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    # Track the number of turns remaining.
    turns = check_answer(answer,guess,turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return #like exit from function (function without output)
    elif guess != answer:
      print("Guess again.")
  
  
game()    
    
  
    # if turns == 0:
      # print("You've run out of guesses, you lose.")
    
      


# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

