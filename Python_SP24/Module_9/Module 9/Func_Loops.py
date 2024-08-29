
# Topics: Functions using Loops

# program discription

'''
Use functions to do the following:
    - Get the number of people vaccinated in a week.
    - find the total number of people vaccinated in a week.
    - print the total
'''

def getInput(i):
    num = int(input('Enter the number of people vaccinated on day #' + str(i) + ': '))
    return num

def findTotal():
    total = 0
    for i in range(1, 8):
        numVaci = getInput(i)
        total += numVaci
    return total 

def printTotal(total):
    print('Total vaccinated: ', total)

def main():
    total = findTotal()
    printTotal(total)

main()