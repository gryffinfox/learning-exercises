# Snake test is a first draft of the project snake booping game.
# I do not use OOP in this version.

import random                           

health_bar = 5                                                                              # Health tracker (or HP, maximum is 5)
point_bar = 0                                                                               # Point tracker
list_of_snakes = ['Cottonmouth', 'Python', 'Viper', 'Boa', 'Rattlesnake']                   # List of snakes that can appear in the game.                                                
actions = ['bite', 'hiss', 'coil']                                                          # List of snake's actions in the game

username = input('Hello, would you like to play a game? \nEnter your name: ')               # User input of the player's name.

for x in range(0, 5):                                                                       # Loop to generate five random snakes from a list_of_snakes.
    random_snake = random.choice(list_of_snakes)
    print(random_snake, 'appears.')                                                         # Generated snake makes an appearence.
    wanna_boop = input('Do you want to boop it? Y/N     ')                                  # Player has a choice - to boop or not to boop.

    if wanna_boop.lower() in ['y', 'yea', 'yeah', 'yes']:                                   # If player wants to boop the snake, random reaction will be chosen.
        snake_action = random.choice(actions)
        
        if snake_action == 'bite':                                                          # Bite - player loses HP and gains points.
            health_bar = health_bar - 4
            point_bar = point_bar + 5
            print(random_snake, 'bit you!')
            print('You have', health_bar, '♥ and', point_bar, 'points!\n')                  # Player's overview - how many point and HP he or she has
            
            if health_bar <= 0:                                                             # If the HP bar goes on or under zero, game is over.
                print('Game over! You gained', point_bar, 'points.')
                break
    
        elif snake_action == 'hiss':                                                        # Hiss - player loses HP and gains points
            health_bar = health_bar - 1
            point_bar = point_bar + 2
            print(random_snake, 'hissed at you!')
            print('Žížalka:', random_snake, 'scared you. Now you have', health_bar, '♥ and', point_bar, 'points!\n')
            
            if health_bar <= 0:
                print('Game over, ', username, '! You gained', point_bar, 'points.')
                break
        
        elif snake_action == 'coil':                                                        # Coil - player gains points.
        
            health_bar = health_bar + 0
            point_bar = point_bar + 1
            print(random_snake, 'coiled!')
            print('Žížalka: No pain, little gain! You have', health_bar, '♥ and', point_bar, 'points!\n')
    
    elif wanna_boop.lower() in ['n', 'no', 'nooo']:
        print('Žížalka: In the nature it is always a smart choice to leave snake alone but in this game you dont gain anything. You have', health_bar, '♥ and', point_bar, 'points!\n')
    
    else:
        print('Žížalka: Not a valid answer - reply Y for yes or N for no. Let me ask again.')

