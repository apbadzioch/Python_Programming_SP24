# global constants
TITLE = "Welcome to the sum of 2 numbers program!"
LINE = "-" * len(TITLE)

# Defining the function that will be used to get numbers.
def getNumber():
    num1 = int(input('Input a number: '))
    return num1

# Defining the function that will be used to find total.
def findTotal(num1, num2):
    total = num1 + num2
    return total

# Defining the function that will be used to print.
def printTotal(num1, num2, total):
    print(num1, '+', num2, '=', total)

# The main script that will call the function above.
def main():
    print(TITLE)
    print(LINE)
    num1 = getNumber()              # value returning function call w/o arguments (nothing within the parentheses)
    num2 = getNumber()              # value returning function call w/o arguments (nothing within the parentheses)
    total = findTotal(num1, num2)   # value returning function call w/- arguments  (something in the paraentheses)
    printTotal(num1, num2, total)   # void function w/- arguments
    print(LINE)

main()                              # void function w/o arguments
'''
print(TITLE)
print(LINE)

num1 = int(input("Input a number: "))
num2 = int(input("Input another number: "))
total = num1 + num2
print(num1, '+', num2, '=', total)

print(LINE)
'''

