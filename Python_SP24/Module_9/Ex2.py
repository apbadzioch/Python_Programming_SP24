# Topics: Functions using loops

# program description

'''
Use functions to do the following:
   - Receive the number of people vaccinated in a week
   - find the total number of people vaccinated in a week 
   - print the total

For example:
Enter number of people vaccinated on Day #1: 1000
Enter number of people vaccinated on Day #2: 10000
Enter number of people vaccinated on Day #3: 0
Enter number of people vaccinated on Day #4: 1111
Enter number of people vaccinated on Day #5: 222
Enter number of people vaccinated on Day #6: 33
Enter number of people vaccinated on Day #7: 8888
Total vaccinated = 21254 
'''

def main():
    total = findTotal()                 # value returning function call w/o arguments
    printResult(total)                  # void function call w/- arg    

def findTotal():
    total = 0
    for i in range(1, 8):
        numVaccinated = getInput(i)     # value returning function call w/- arg
        total += numVaccinated
    return total

def getInput(i):
    numVaccinated = int(input("Enter number of people vaccinated on Day #" + str(i) + ": "))
    return numVaccinated
    
def printResult(total):
    print("Total vaccinated =", total)
    
main()                                  # void function call w/o args





