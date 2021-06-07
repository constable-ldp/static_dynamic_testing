### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
      if card.value = 1: # should have double equals
      return True # return should be indented
    else # : is missing
      return False
   

  dif highest_card(self, card1 card2): # should be def not dif and comma missing between card1 and card2
  if card1.value > card2.value: #if else should be indented
    return card # card is not defined should be card1 or card2
  else:
    return card2
  


def cards_total(self, cards): #function should be indented as it is part of the class
  total # total needs to be defined
  for card in cards:
    total += card.value
    return "You have a total of" + total #string cannot be concatenated to a integer 
  
```
