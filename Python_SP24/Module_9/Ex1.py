# CHAPTER: FUNCTIONS
# Topics:
# void function call w/o arguments
# void function call w/- arguments
# value returning function call w/o arguments
# value returning function call w/- arguments

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

# global constants
TITLE = "Welcome to sum of 2 numbers program!"
LINE = '-' * len(TITLE)

# main function definition of void function w/- args
def main():
    print(TITLE)
    print(LINE)
    num1 = getNumber()              # value ret func w/o args
    num2 = getNumber()
    total = findTotal(num1, num2)   # value ret func w/- args
    printTotal(num1, num2, total)   # void func call w/- args
    print(LINE)

# findTotal function definition of value returning function w/- args
def findTotal(num1, num2):
    total = num1 + num2
    return total

# getNumber function definition of void function w/o args
def getNumber():
    num = int(input("Enter a number: "))
    return num

# printTotal function definition of void function w/- args
# def printTotal(n1, n2, t):
def printTotal(num1, num2, total):
    #print(n1, "+", n2, "=", t)   
    print(num1, "+", num2, "=", total)    
    
main()                              # void func call w/o args














