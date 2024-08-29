# Topics:
# How functions can be used as MODULES

# program description
'''
Use functions to do the following:
   - print the program title "Welcome to sum of 2 numbers program!"
   - have the user enter 2 numbers
   - find the sum of 2 numbers
   - print the sum

For example:
Welcome to sum of 2 numbers program!
------------------------------------
Enter a number: 6
Enter a number: 10
6 + 10 = 16
------------------------------------
'''

import mod1
import mod2

def printLine():
    print(format('', '~>40s'))

def main():
    mod1.printTitle()
    num1, num2 = mod1.getNumbers()       
    total = mod2.findTotal(num1, num2)
    mod2.printTotal(num1, num2, total)
    printLine()

main()          














