# Topics: value returning function which returns MULTIPLE VALUES (more than one)

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

def main():
    printTitle()
    num1, num2 = getNumbers()       # returning multiple values
    total = findTotal(num1, num2)   
    printTotal(num1, num2, total)
    print(LINE)

def printTitle():
    print(TITLE)
    print(LINE)

def findTotal(num1, num2):
    total = num1 + num2
    return total
    
def getNumbers():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    return num1, num2
    
def printTotal(num1, num2, total):
    print(num1, "+", num2, "=", total)    
    
main()                      














