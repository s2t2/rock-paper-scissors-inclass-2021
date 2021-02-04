# game.py

import random

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
# ACCEPT USER INPUT
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

print(f"You chose: {user_choice}")

#
# VALIDATE USER INPUT
#
# ... adapted from Kevin's solution during class

options = ["rock", "paper", "scissors"]

if user_choice.lower() not in options:
    print("OOPS, please choose a valid option and try again")
    exit()

#
# GENERATE COMPUTER INPUT
#
# ... adapted from: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")

#
# DETERMINE THE WINNER
#
# ... adapted from code Will shared during class

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
