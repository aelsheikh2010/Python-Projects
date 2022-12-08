#!/usr/bin/env python
# coding: utf-8

# In[ ]:


rock = '''
    _______
---'   ____)
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
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list_choices=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice > 2 or user_choice<0:
    print("you have entered invalid choice")
else:
    print(list_choices[user_choice])
    computer_choice=random.randint(0,2)
    print(f"computer chose:{list_choices[computer_choice]}")
     
    if user_choice==0 and computer_choice==2:
        print("You win")
    elif user_choice==0 and computer_choice==1:
        print("You lose")
    elif user_choice==2 and computer_choice==1:
        print("You win")
    elif user_choice==2 and computer_choice==0:
        print("You lose")
    elif user_choice==1 and computer_choice==0:
        print("You win")
    elif user_choice==1 and computer_choice==2:
        print("You lose")
    elif user_choice==computer_choice:
        print("it's a draw")

# # else:
# #     print("you have entered an invalid number")

