#!/usr/bin/env python
# coding: utf-8

# In[2]:


from blind_auction_logo import logo
from IPython.display import clear_output
#HINT: You can call clear_output() to clear the output in the console.
print(logo)
print("Welcome to secret auction program.\n")
def high_bids(bidding_records):
  #{"ahmed": 123,"toto":234,"soso":700}
  high_val=0
  winner=""
  for key in bidding_records:
    bid_amount= bidding_records[key]
    if bid_amount>high_val:
      high_val=bid_amount
      winner=key
  print(f"The winner is {winner} with a bid of ${high_val}")
bid_dic={}
should_continue=True
while should_continue:
  name=input("what is your name? ")
  bid=int(input("what's your bid?: $"))
  bid_dic[name] = bid
  choise=input("Are there any other bidders? Type 'yes' or 'no'\n")
  if choise == "no":
    should_continue=False
    clear_output()
    high_bids(bid_dic)
    print(logo)
  else:
    should_continue=True
    clear_output()
   


# In[ ]:




