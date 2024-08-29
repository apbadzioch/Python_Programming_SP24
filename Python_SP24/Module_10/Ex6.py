# Searching lists
'''
Randomly generate 6 lotto numbers in the range 1-54.
Receive the winning number in the range 1-54.
Search and print appropriate message if winning number exists or not.
Modularize the program using functions

# Test Run 1
Enter number in the range 1-54: 111
Enter number in the range 1-54: 0
Enter number in the range 1-54: 7
Better luck next time!

# Test Run 2
Enter number in the range 1-54: 53
Congratulations! You have won the lotto :)
'''

import random

def populateList(lst):
    for i in range(6):
        randNum = random.randint(1, 54)
        lst.append(randNum)

def getWinNum():
    while True:
        winNum = int(input("Enter number in the range 1-54: "))
        if winNum >= 1 and winNum <= 54: break;
    return winNum

def printResults(winNum, lst):
    win = False
    for i in lst:
        if i == winNum:
            print("Congratulations! You have won the lotto :)")
            win = True
            break
    if not win: print("Better luck next time!")
    
def main():
    lst = []
    populateList(lst)
    winNum = getWinNum()
    printResults(winNum, lst)
    
main()

# OUTPUT
# Test Run 1
'''
Enter number in the range 1-54: 111
Enter number in the range 1-54: 0
Enter number in the range 1-54: 7
Better luck next time!
'''
# Test Run 2
'''
Enter number in the range 1-54: 53
Congratulations! You have won the lotto :)
'''
