
TITLE = "Welcome to the sum of 2 numbers program!"
LINE = "-" * len(TITLE)

def printTitle():
    print(TITLE)
    print(LINE)

def getNum():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    return num1, num2