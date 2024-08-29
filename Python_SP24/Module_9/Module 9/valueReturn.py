# Topics: Value returning function that returns MULTIPLE VALUES

# Global Constants

TITLE = "Welcome to the sum of 2 numbers program!"
LINE = "-" * len(TITLE)

def printTitle():
    print(TITLE)
    print(LINE)

def getNum():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    return num1, num2

def findTotal(num1, num2):
    total = num1 + num2
    return total

def printTotal(num1, num2, total):
    print(num1, "+", num2, "=", total)

def main():
    printTitle()
    num1, num2 = getNum()
    total = findTotal(num1, num2)
    printTotal(num1, num2, total)
    print(LINE)

main()