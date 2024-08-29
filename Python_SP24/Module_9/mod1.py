# module getNumbers.py

# global constants
TITLE = "Welcome to sum of 2 numbers program!"
LINE = '-' * len(TITLE)

def printTitle():
    print(TITLE)
    print(LINE)
    
def getNumbers():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    return num1, num2
        
    
