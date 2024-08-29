# MadLib Example Program:
# Name: Enter your fullname here
# Lab: MadLib Program
# Description: Mad Lib program shows the usage of inputting data and
#        printing it back out intermixed with set information.


# Algorithm:
# a. Declare three string variables: pluralnoun1, noun1, adjective1
# b. Declare an integer variable: num1
# c. Ask user to enter a pluralnoun, noun, adjective, and number
# g. Display the constructed message using the contents of variables:
#     pluralnoun1, noun1, adj1, and num1 in the following story:

# Mad Libs - Puzzles example:
#        In the early 1900s, crossword <pluralnoun1> only appeared in children's
#         books. Today, <noun1> puzzles are in almost <number1> magazines
#         printed in the U.S. and throughout the whole <adjective1> world.

# Set variables to default (unused) values
# We set the first three to an empty string since they will eventually hold a string
# We set the num1 variable to an integer 0 since we know it will hold an int later

pluralnoun1 = ""    # Set to an empty string, two quotes next to each other
noun1 = ""           # Set to an empty string
adjective1 = ""     # Set to an empty string
num1 = 0            # Set to 0

pluralnoun1 = input("Enter a plural noun: ")
noun1 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
num1 = int(input("Enter a number: "))

print("\nMad Libs - Puzzles\n")
print("In the early 1900s, crossword", pluralnoun1)
print("only appeared in children's books.")
print("Today,",noun1,"puzzles are in almost", num1)
print("magazines printed in the U.S. and")
print("througout the whole", adjective1,"world.")

# OUTPUT
'''
Enter a plural noun: cats
Enter a noun: dog
Enter an adjective: colorful
Enter a number: 9857

Mad Libs - Puzzles

In the early 1900s, crossword cats
only appeared in children's books.
Today, dog puzzles are in almost 9857
magazines printed in the U.S. and
througout the whole colorful world.
'''
