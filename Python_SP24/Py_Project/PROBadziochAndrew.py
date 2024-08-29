'''
Name: Andrew Badzioch
Date: April 30, 2024
Name: Rock, Paper, Scissors
Description: The classic game of "Rock, Paper, Scissors" where the player competes against the computer. Whe starting the game, the player
            is greeted with a welcome message and are prompted to choose between rock, paper, or scissors. The computer then randomly selects
            its choice and the winner is determined based on the classic rules of the game. The result is displayed, indicating whether the 
            user wins, loses, or draws with the computer. This game will continue until the player opts out by typing 'n' when prompted after
            each round.
'''

# Import the random module from the Python library.
import random

# Global Constants used for the introduction messages, create a separation line, and welcome the player to the game.
GREETING = ("Hello and Welcome to Andy's Rock, Papar, Scissors Game!")
LINE = "-" * len(GREETING)
PLAY = ("Let's Play!")

# The function that asks the user for a choice of rock, paper, or scissors and will loop unless it is a valid input.
def getUserChoice():
    while True:
        userChoice = input("Please choose: r for rock, p for paper, or s for scissors: ").lower()
        if userChoice in ['r', 'p', 's']:
            return userChoice
        else:
            print("Please choose a valid option.")

# Function that randomly selects rock, paper, or scissors for the computer's choice by calling the '.choice()' function from the imported 'random' module.           
def getCompChoice():
    choices = ('r', 'p', 's')
    return random.choice(choices)

# Function that determines the winner of the game based on the choices made by the user and computer. After comparing the choices, it returns a message
# stating the results (tie, user won, or computer won) as well as formating using the dictionary to give the corresponding definition for better readability.
def getWinner(userChoice, compChoice):
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    if userChoice == compChoice:
        return "It's a Draw!"
    if (userChoice == 'r' and compChoice == 's'):
        return (f"You win! {choices[userChoice]} crushes {choices[compChoice]}")
    elif (userChoice == 's' and compChoice == 'p'):
        return (f"You win! {choices[userChoice]} cut {choices[compChoice]}")
    elif (userChoice == 'p' and compChoice == 'r'):
        return (f"You win! {choices[userChoice]} covers {choices[compChoice]}")
    else:
        return (f"Sorry, you lose, the computer chose {choices[compChoice]}.")

# The main function of the game, displaying the initial greeting, asks the user for their choice, generates the computer choice, determines the winner,
# and will keep playing until the user chooses not to continue.
def r_p_s():
    print()
    print(GREETING)
    print(PLAY)
    print(LINE)
    while True:
        userChoice = getUserChoice()
        compChoice = getCompChoice()
        print(getWinner(userChoice, compChoice))
        print()
        playAgain = input("Would you like to keep playing? y/n: ").lower()
        if playAgain == 'n':
            print("Thanks for playing!")
            print()
            break
        
r_p_s()