import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum): 
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    print("")
    playerchoice = input(
        "Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
    if playerchoice not in ["1", "2", "3"]: # all user input is String
        print("You must enter 1, 2, or 3.")
        return play_rps()
    player = int(playerchoice)
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("")
    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("Python wins!")
    print("\nPlay again?")
    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue # if it's not y or q, it will restart the loop and ask the user again
        else:
            break # if user enters y or q, the loop will stop
    if playagain.lower() == "y":
        return play_rps() # after successful input by user, recursive call to function to restart game
    else:
        print("Thank you for playing!\n")
        sys.exit("Bye!")
play_rps()
