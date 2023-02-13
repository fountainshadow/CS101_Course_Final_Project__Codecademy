# Black Jack Program.
import random
from random import sample

# Options from a deck of cards.
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = sample(deck, 2)

# FUNCTIONS
# Sum of Cards
def card_sum(user_cards):
    sum = 0
    for i in user_cards:
        sum += i
    print(f"Your current total is: {sum}")

# Want Another Card - Question
def stick_or_twist():
    decision = input("Would you like another card? Y/N: ")
    if decision == 'Y':
        twist()
    elif decision == 'N':
        stick()
    else:
        print("Error")

# Draw Again
def twist():
    user_cards.extend(sample(deck, 1))
    print(f"You currently hold the cards: {user_cards}")
    user_sum = card_sum(user_cards)

# Stick With Cards
def stick():
    print(f"You are currently holding the cards: {user_cards}")
    user_sum = card_sum(user_cards)

# INTRO
print("Welcome to Black Jack! You will be playing against the banker.")
name = input("What is your name? ")
print(f"WELCOME TO THE GAME {name}!")

# STARTING POINT
print(f"Your starting cards are: {user_cards}. You current total is: {sum(user_cards)} out of 21.")

stick_or_twist()


