# Name : Andy Badzioch
# Date : Feb. 20, 2024
# Program : Chapter 3 - Selections
# Description : This is a practice program with if/elif/else asking the user to input integers and a mathmatical function. The program then cycles
#               the given code, sending up errors if there are any, then prints the line of the first number, second number, what they wanted to do 
#               the answer.

# Constants
GREETING = "Hey"
TITLE = "Welcome to the Python Calculator SIM!"
LINE = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
DIV_BY_ZERO = "Sorry, you can't divide by zero 😕"
INVALID = "is INVALID"
ASSIGN_OP = '='


#input user's name
nombre = input('Hello, what should I call you?: ')

#Heading Display
print(LINE)
print(GREETING, nombre, TITLE)
print(LINE)

#input for user's integers
intOne = int(input('Please enter an integer, e.g. 4, 5, 13: '))
intTwo = int(input('Please enter another integer: '))
opSym = input('Please enter what you would like to do (**, +, -, *, /, //, or %): ')

# Begin if/elif/else
if opSym == '**':
    print(intOne, opSym, intTwo, ASSIGN_OP, intOne ** intTwo)
elif opSym == '+':
    print(intOne, opSym, intTwo, ASSIGN_OP, intOne + intTwo)
elif opSym == '-':
    print(intOne, opSym, intTwo, ASSIGN_OP, intOne - intTwo)
elif opSym == '*':
    print(intOne, opSym, intTwo, ASSIGN_OP, intOne * intTwo)
elif intTwo == 0 and (opSym == '/' or opSym == '//' or opSym == '%'):
    print(DIV_BY_ZERO)
else:
    if opSym == '/':
        print(intOne, opSym, intTwo, ASSIGN_OP, intOne / intTwo)
    elif opSym == '//':
        print(intOne, opSym, intTwo, ASSIGN_OP, intOne // intTwo)
    elif opSym == '%':
        print(intOne, opSym, intTwo, ASSIGN_OP, intOne % intTwo)
    else:
        print(opSym, INVALID)