# Program description: Functions and Lists
'''
Receive the number of people vaccinated in a week
Print the day lowest and highest number of people were vaccinated

Example:
Enter number of people vaccinated on Sunday: 6
Enter number of people vaccinated on Monday: 7
Enter number of people vaccinated on Tuesday: 11
Enter number of people vaccinated on Wednesday: 111
Enter number of people vaccinated on Thursday: 1
Enter number of people vaccinated on Friday: 2
Enter number of people vaccinated on Saturday: 3
Number of people vaccinated on Thursday is lowest = 1
Number of people vaccinated on Wednesday is highest = 111
'''
NUM_DAYS = 7
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def populateList(lst):
    for i in range(NUM_DAYS):
        numVaccinated = int(input("Enter number of people vaccinated on " + DAYS[i] + ": "))
        lst.append(numVaccinated)

def findLo(lst):
    loIndex = 0
    loElem = lst[0]
    #for i in lst:
    for i in range(1, len(lst)):
        if lst[i] < loElem:
            loIndex = i
            loElem = lst[i]
    return loIndex

def findHi(lst):
    hiIndex = 0
    hiElem = lst[0]
    #for i in lst:
    for i in range(1, len(lst)):
        if lst[i] > hiElem:
            hiIndex = i
            hiElem = lst[i]
    return hiIndex

def printLoHi(loIndex, hiIndex, lst):
    print("Number of people vaccinated on " + DAYS[loIndex] + " is lowest =", lst[loIndex])
    print("Number of people vaccinated on " + DAYS[hiIndex] + " is highest =", lst[hiIndex])

def main():
    lst = []
    populateList(lst)
    loIndex = findLo(lst)
    hiIndex = findHi(lst)
    printLoHi(loIndex, hiIndex, lst)
        
main()

# OUTPUT
'''
Enter number of people vaccinated on Sunday: 66
Enter number of people vaccinated on Monday: 1
Enter number of people vaccinated on Tuesday: 4
Enter number of people vaccinated on Wednesday: 7777
Enter number of people vaccinated on Thursday: 5
Enter number of people vaccinated on Friday: 1111
Enter number of people vaccinated on Saturday: 11
Number of people vaccinated on Monday is lowest = 1
Number of people vaccinated on Wednesday is highest = 7777
'''
