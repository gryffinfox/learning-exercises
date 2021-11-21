# This program is a classic game called Rock, paper, scissors
# You play against computer that will generate random choice.

import random
random_choice = random.randint(0,2)                             # Computer finds random number between 0 and 2 and associate it with one of three choices

if random_choice == 0:
  random_choice = "rock"
  
elif random_choice == 1:
    random_choice = "paper"
    
elif random_choice == 2:
    random_choice = "scissors"
    
user_choice = input("Rock, paper, scissors? ")                  # User gets asked what is he or she going to choose.

while (user_choice != "rock" and                                # If the reply isn't rock, paper or scissors, he will get asked again.
       user_choice != "scissors" and
       user_choice != "paper"):
    print("Not a valid answer, try again.")
    user_choice = input("Rock, paper, scissors? ")

print("Computer:", random_choice, "x User:", user_choice)       # Both choices - of a computer and a user - are being compaired and evaluated.

if random_choice == user_choice:
    winner = "Tie!"
    print(winner)
    
elif random_choice == "paper" and user_choice == "rock":        # Computer wins, paper wraps rock.
    print("Paper wraps the rock. Computer won, you lost.")

elif random_choice == "rock" and user_choice == "scissors":     # Computer wins, rock blunts scissors.
    print("Rock blunts scissors. Computer won, you lost.")
    
elif random_choice == "scisors" and user_choice == "paper":     # Computer wins, Scissors cuts paper.
    print("Scissors cuts paper. Computer won, you lost.")


elif user_choice == "paper" and random_choice == "rock":        # User wins, paper wraps rock.
    print("Paper wraps the rock. You won, computer lost.")

elif user_choice == "rock" and random_choice == "scissors":     # User wins, rock blunts scissors.
    print("Rock blunts scissors. You won, computer lost.")
    
elif user_choice == "scisors" and random_choice == "paper":     # User wins, Scissors cuts paper.
    print("Scissors cuts paper. You won, computer lost.")
    

    
    
