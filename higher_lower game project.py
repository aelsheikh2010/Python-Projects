#Higher Lower Game
#import art and random
#print logo
#random choice from list 
#compare between number of followers for each choice 
#if user choose the highest number of followers of two choices 
#then he win a point and continue play
#then the choice with high number of score become the first choise if not 


import random 
from higher_lower_art import logo,vs
from higher_lower_data import data
from replit import clear

def choices():
   """return random select from list of dictionary"""
   return random.choice(data)

def format_data(choice_data):
  name = choice_data['name']
  description = choice_data['description']
  country = choice_data['country']
  return f"{name}, {description}, {country}"

def check_answer(choice_A,choice_B):
  guess = input("Who has more followers? Type 'A' or 'B': ").lower() 
  follower_list = [choice_A['follower_count'],choice_B['follower_count']]
  print(follower_list)
  high_follower = max(follower_list)
  if high_follower == follower_list[0]:
    return guess == "a"
  else:
    return guess == "b"
  return high_follower
 



def game():
  print(logo)
  choice_A = choices()
  choice_B = choices()
  score = 0
  should_coninue = True
  while should_coninue:
    choice_A = choice_B
    choice_B = choices()
    print(f"Compare A : {format_data(choice_A)}")
    print(vs)
    print(f"Against B: {format_data(choice_B)}")
  
    is_correct = check_answer(choice_A,choice_B)
    print(logo)
    clear()
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      should_coninue = False
      print(f"Sorry, that's wrong. Final score: {score}")
      

game()
