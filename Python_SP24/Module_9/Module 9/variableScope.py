
# Topic: Local/Global scope of variables
# It isn't good practice to make valiables Global. But can be over ridden.


TITLE = "Welcome to the sum of 2 numbers program!"
LINE = "-" * len(TITLE)

total = 0                                               # vaiable has been made Global

def printTitle():
    print(TITLE)
    print(LINE)

def getNum():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    return num1, num2

def findTotal(num1, num2):
    #print(total)                                       # total has been used from Global
    total = num1 + num2
    return total                                        # taken out of commission
    #print(total)                                       # total has been overridden locally
                                                        # you must return what you are looking for locally
def printTotal(num1, num2, total):
    print(num1, "+", num2, "=", total)

def main():
    printTitle()
    num1, num2 = getNum()
    total = findTotal(num1, num2)
    printTotal(num1, num2, total)
    print(LINE)

main()
