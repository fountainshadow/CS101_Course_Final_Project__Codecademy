# Black Jack Program.
import random
from random import sample

# Options from a deck of cards.
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Intro
print("Welcome to Black Jack! You will be playing against the banker.")
name = input("What is your name? ")
print(f"Welcome to the game {name}!")

# Starting Point
user_cards = sample(cards, 2)
print(f"Your starting cards are: {user_cards}")
user_sum = 0
for i in user_cards:
    user_sum += i
print(f"You current total is: {user_sum} out of 21")

# FUNCTIONS
# Another Card
def decision():
    decision = input("Would you like another card? Y/N: ")
    if decision == 'Y':
        draw_card(decision)
    elif decision == 'N':
        draw_card(decision)
# Bust
def bust(choice):
    user_sum = 0
    if user_sum > 21:
        print("You have gone BUST! The banker has won...")
    elif user_sum <= 21:
        draw_card()

# Stick or Twist
def draw_card(choice):
    if choice == 'Y':
        user_cards.extend(sample(cards, 1))
        print(f"You currently hold the cards: {user_cards}")
        user_sum = 0
        for i in user_cards:
            user_sum += i
        print(f"You current total is: {user_sum} out of 21")
        decision()
    elif choice == 'N':
        print(f"You have stuck with the cards: {user_cards}")
    else:
        print("Error.")

choice = decision()
print(choice)
draw_card(choice)