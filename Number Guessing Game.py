# BLX-UNKNOWN-0
# PROJECT 2 // NUMBER GUESSING GAME
# Learned: import, random, while loops, if/elif/else

import random

def GAME():
    print("...NUMBER GUESSING GAME...")
    print("I'm thinking between number 1 - 100 , can you guess it?")

    secret = random.randint(1, 100)
    tries = 0

    while True :
        try:
            guess = int(input("Enter your guess : " ))
        except ValueError:
            print("Number is invalid ;\n ")
            continue

        tries += 1

        if guess > secret:
            print("your guess is too high, try lower")
        elif guess < secret :
            print("your guess is too low, try higher")
        else :
            print(f"correct : you got that in {tries} tries")
            break
GAME()