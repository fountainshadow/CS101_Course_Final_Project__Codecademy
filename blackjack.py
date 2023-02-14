# Black Jack Program.
import random
from random import sample
import time

# Options from a deck of cards.
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = sample(deck, 2)
dealer_cards = sample(deck, 2)

# FUNCTIONS
# Calculate If Bust
def bust_or_not(user_cards):
    if sum(user_cards) > 21:
        print("You have gone BUST! The dealer has won.")
    elif sum(user_cards) <= 21:
        choice = input("Would you like another card? Y/N: ")
        if choice == 'N':
            stick()
        else:
            twist()
    else: 
        print('Error in bust or not function')

# Draw Again
def twist():
    user_cards.extend(sample(deck, 1))
    print(f"You currently hold the cards: {user_cards}. Your current total is: {sum(user_cards)}.")
    bust_or_not(user_cards)

# Dealer Function
def dealer(dealer_cards):
    while sum(dealer_cards) < 17:
        dealer_cards.extend(sample(deck,1))
    print(f"The Dealer's Cards are: {dealer_cards}. Their total is: {sum(dealer_cards)}.")
    if (sum(dealer_cards) >= sum(user_cards)) and (sum(dealer_cards) <= 21):
        print("THE DEALER HAS WON!")
    elif (sum(user_cards) > sum(dealer_cards)) and (sum(dealer_cards) <= 21):
        print("YOU HAVE WON!!")

# Stick With Cards
def stick():
    print(f"You are currently holding the cards: {user_cards}. Your current total is: {sum(user_cards)}.")
    time.sleep(0.5)
    print("Let's see what cards the dealer is holding...")
    time.sleep(0.5)
    print(f"The dealer's starting cards are: {dealer_cards}")
    time.sleep(1)
    dealer(dealer_cards)


# -----
# INTRO
print("Welcome to Black Jack! You will be playing against the Dealer.")
name = input("What is your name? ")
print(f"WELCOME TO THE GAME {name}!")

# STARTING POINT
print(f"Your starting cards are: {user_cards}. You current total is: {sum(user_cards)} out of 21.")

bust_or_not(user_cards)