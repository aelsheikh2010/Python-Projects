#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Password Generator Project (**** my solution)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
list_letters=[]
for i in range(nr_letters):
    list_letters.append(random.choice(letters))
print(list_letters)   
        
list_symbols=[] 
for s in range(nr_symbols):
    list_symbols.append(random.choice(symbols))
print(list_symbols)
    
list_numbers=[]
for l in range(nr_numbers):
    list_numbers.append(random.choice(numbers))
print(list_numbers) 
#concatnating 3 lists into one list
password_list=list_letters+list_symbols+list_numbers
random.shuffle(password_list)
print(password_list)
#create one variable from password list
password=""
for c in password_list:
    password+=c
print(f"Your password is: {password}")

