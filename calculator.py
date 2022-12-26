#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#calculator
#add function
from calculator_art import logo
def add(n1, n2):
    return n1 + n2


#subtract function
def subtract(n1, n2):
    return n1 - n2


#multiply function
def multiply(n1, n2):
    return n1 * n2


#divide function
def divide(n1, n2):
    return n1 / n2


#create a new dictionary called operations
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
def calculator():
  print(logo)
  num1 = float(input("what's the first number?: "))
  for symbol in operations:
      print(symbol)
    
  should_coninue = True
  while should_coninue: 
    symbol_operation = input("pick an operation: ")
    num2 = float(input("what's the next number?: "))
    calculation_function = operations[symbol_operation]
    answer = calculation_function(num1, num2)
    print(f"{num1} {symbol_operation} {num2} = {answer}")
    prog_continue = input(f"Typy 'y' to coninue calculating with {answer},or type 'n' to start a new calculation: ")
    if prog_continue =="y":
      num1 = answer
    else:
      should_coninue = False
      calculator()
calculator()


# In[ ]:




