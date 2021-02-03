# game.py

import random
#from random import choice

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
# asking user for an input
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

print(f"You chose: {user_choice}")

#
# validate the user selection
#
# stop the program (not try to determine the winner)
# ... if the user choice is invalid

#user_choice.lower()

#if user_choice in options:
#    #print("GOOD")
#    pass
#else:
#    print("OOPS, please choose a valid option and try again")
#    exit()

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("OOPS, please choose a valid option and try again")
    exit()

#
# simulating a computer input
#

#computer_choice = "paper"


#foo = ['a', 'b', 'c', 'd', 'e']
#computer_choice = random.choice(foo)

computer_choice = random.choice(options)
#computer_choice = choice(options)

print(f"The computer chose: {computer_choice}")



#
# determine who won
#

if user_choice == computer_choice:
    print("It's tie!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Congrats")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "rock":
    print("Oh! The computer won, that's ok!")








print("Thanks for playing. Please play again!")


#
