# BLX-UNKNOWN-0
# PROJECT 6 // ROCK PAPER SCISSORS

import random

NAMES = {1: "Rock", 2: "Paper", 3: "Scissors"}


WINS_AGAINST = {1: 3, 2: 1, 3: 2}

def game():
    print("...ROCK PAPER SCISSORS...")
    print(" 1=Rock  2=Paper  3=Scissors  0=Quit")

    while True:
        com = random.randint(1, 3) 

        try:
            player = int(input("\nYour choice: "))
        except ValueError:
            print("Enter a number!")
            continue

        if player == 0:
            print("Bye!, Have a great day!")
            break
        if player not in [1, 2, 3]:
            print("Choose 1, 2 or 3 only.")
            continue

        print(f"You: {NAMES[player]}  |  Computer: {NAMES[com]}")

        if player == com:
            print(" Tie!")
        elif WINS_AGAINST[player] == com:  #  clean win check
            print(" You Win!")
        else:
            print(" You Lose!")

game()
