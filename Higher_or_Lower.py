#This program asks the user to guess a number between 1 and 1000. If the guess is lower, then it prints lower. If higher, it prints lower.

# TO DO:
# Find a way to replay the game.
# Provide a counter of how many times you guessed.
# Play vs. computer mode.

import random

#MODE RANGES:
easy = int(random.randrange(1,100))
medium = int(random.randrange(1,1000))
hard = int(random.randrange(1,10000))

#INTRO INTERFACE:
print("In this game, you have to guess a number within a range.")
mode = input('Would you like to play on easy, medium or hard? Type in e, m or h:\n')

#MODES
def easy_mode():
    a = int(input("\nGuess a number between 1 and 100: \n"))
    if easy < a < 101:
        print("LOWER")
        easy_mode()
    elif 0 < a < easy:
        print("HIGHER")
        easy_mode()
    elif a <= 0:
        print('Guess is below the range')
        easy_mode()
    elif a >= 101:
        print('Guess is above the range')
        easy_mode()
    else:
        print("\nCONGRATS! You guessed it!")
        replay()

def medium_mode():
    b = int(input("\nGuess a number between 1 and 1000: \n"))
    if medium < b < 1001:
        print("LOWER")
        medium_mode()
    elif 0 < b < medium:
        print("HIGHER")
        medium_mode()
    elif b <= 0:
        print('Guess is below the range')
        medium_mode()
    elif b >= 1001:
        print('Guess is above the range')
        medium_mode()
    else:
        print("\nCONGRATS! You guessed it!")
        replay()

def hard_mode():
    c = int(input("\nGuess a number between 1 and 10000: \n"))
    if hard < c < 10001:
        print("LOWER")
        hard_mode()
    elif 0 < c < hard:
        print("HIGHER")
        hard_mode()
    elif c <= 0:
        print('Guess is below the range')
        hard_mode()
    elif c >= 10001:
        print('Guess is above the range')
        hard_mode()
    else:
        print("\nCONGRATS! YOU GUESSED IT!")
        replay()

#REPLAY
def replay():
    yes_no = input("\nWould you like to play again? (Type in yes or no): \n").upper()
    if yes_no == 'NO':
        pass
    elif yes_no == 'YES':
        mode = input('\nWould you like to play on easy, medium or hard? Type in e, m or h:\n')
        if mode == 'e':
            easy_mode()
        elif mode == 'm':
            medium_mode()
        elif mode == 'h':
            hard_mode()
        else:
            print('Invalid input. Please try again.')
    else:
        print("Invalid response.")
        replay()

#MODES
if mode == 'e':
    easy_mode()
elif mode == 'm':
    medium_mode()
elif mode == 'h':
    hard_mode()
else:
    print('Invalid input. Please try again.')



    
    


