# Topics: function with DEFAULT ARGUMENTS

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
16
------------------------------------
'''

# global constants
TITLE = "Welcome to sum of 2 numbers program!"
LINE = '-' * len(TITLE)

def main():
    printTitle()
    num1, num2 = getNumbers()       
    total = findTotal(num1, num2)  # no default 
    printTotal(total)

    num1, num2 = getNumbers()
    total = findTotal(num1)         # default num2
    printTotal(total)

    num1, num2 = getNumbers()
    total = findTotal()             # default both num1 and num2
    printTotal(total)    
    print(LINE)

def printTitle():
    print(TITLE)
    print(LINE)

def findTotal(num1=0, num2=0):
    total = num1 + num2
    return total
    
def getNumbers():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    return num1, num2
    
def printTotal(total):
    print(total)    
    
main()                              # void func call w/o args














