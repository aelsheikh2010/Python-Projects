#!/usr/bin/env python
# coding: utf-8

# In[ ]:


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art as a
a.logo
print(a.logo)
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift % 26
    caesar(text,shift,direction)
    result=input("Type 'yes' if you want to go again.otherwise type 'no'..\n")
    if result=="no":
        should_continue=False
        print("good by sir...")
    else:
        should_continue=True
def caesar(text,shift,direction):
    split_text=list(text)
    index_alphabet=[]
    for txt in split_text:
        if txt in alphabet:
            index_text=alphabet.index(txt)
            index_alphabet.append(index_text)
        else:
            index_alphabet.append(txt)
    caesar_list_indx=[]
    for x in index_alphabet:
        if type(x) ==int:
            if direction=="encode":
                x+=shift
            elif direction=="decode":
                x-=shift
            caesar_list_indx.append(x)
        else:
            caesar_list_indx.append(x)
    
    text_caeser=""
    for i in caesar_list_indx:
        if type(i)==int:
            text_caeser+=alphabet[i]
        else:
            text_caeser+=i
    print(f"The {direction} text is {text_caeser}")


# Another way..

# In[ ]:


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art as a
a.logo
print(a.logo)
should_continue=True
while should_continue :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift % 26
    # Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    result=input("Type 'yes' if you want to go again.otherwise type 'no'..\n")
    if result=="no":
        should_continue=False
        print("Good bye")
    else:
        should_continue=True

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(plain_text, shift_amount,cipher_direction):
  end_text = ""
  if cipher_direction=="decode":
      shift_amount *= -1
  for letter in plain_text:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += letter
  print(f"The {cipher_direction} text is {end_text}")  







