# This is a simple version of a card game Black Jack made with Pyladies online courses
# The goal is to get to the total sum of 21 points.

from random import randrange

total = 0

while total < 21:                                           # While loop is set to renew whenever the total is less the 21
    print('You have', total, 'points')
    answer = input('New card? ')                            # Player can always choose if they want to continue.
    
    if answer == 'yes':             
        card = randrange(2, 11)                             # Ace is always 11
        print('You have', card)
        total = total + card
        
    elif answer == 'no':                                    # If player doesn't want to play anymore, the loop will break.
        break
    
    else:
        print('I don\'t understand. Answer yes or no.')

if total == 21:
    print('Congratulations! You won! :)')                   # You win if you have exactly 21 points.
    
elif soucet > 21:
    print('You lost!', total, 'point is too much!')         # You lose if your score is higher then 21.
    
else:
    print('You were missing only', 21 - total, 'points!')   #You lose if your score is lower then 21.
