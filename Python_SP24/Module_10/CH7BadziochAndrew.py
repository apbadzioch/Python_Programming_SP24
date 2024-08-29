'''
Name:           Andrew Badzioch
Date:           April 16, 2024
Program:        Chapter 7 - Lists
Description:    This program collects a user defined list of numbers and performs various analyses on them. 
                It utilizes functions to perform different tasks such as input collection, finding the lowest
                and highest numbers, calculating the total sum and determining the average. The program then 
                displays the results and formatting the average to two decimal points 
'''

# Constants
TITLE = "Welcome to the Number Analysis Program.\n"
LINE = '#' * len(TITLE)
LIST_SIZE = 5

# main function
def main():
    print(TITLE+LINE)
    numsList = []
    numsList = getNums()
    lo = findLo(numsList)
    hi = findHi(numsList)
    total = findTotal(numsList)
    avg = findAvg(numsList)
    displayData(lo, hi, total, avg)

# getNums function: used to get a list of numbers from the user.
def getNums():
    numsList = []                                           # empty list that will store the numbers entered
    for i in range(0, LIST_SIZE):
        nums = int(input("Please enter a number: "))
        numsList.append(nums)
    return numsList

# findLo function: used to find the lowest number from the getNums() function.                                          
def findLo(numsList):
    lo = numsList[0]                                        # initializing the variable lo with the first number in the list
    for num in numsList:                                    # using for loop iterating through all elements in numsList
        if num < lo:                                        # using if to check if less than lo
            lo = num                                        # assigning lowest element to valirable
    return lo

# findHi function: used to find the highest number from the getNums() function, switching hi for lo
def findHi(numsList):
    hi = numsList[0]                                    
    for num in numsList:                            
        if num > hi:
            hi = num
    return hi

# findTotal function: used to sum the numbers from the getNums() function.
def findTotal(numsList):                                    # define function                                    
    total = 0                                               # assign zero to variable 0
    for num in numsList:                                    # for loop iterating through numsList
        total += num                                        # add all elements in numsList
    return total

# findAvg function: used to find the average of the numbers from the getNums() function, using a copy of the above function. 
def findAvg(numsList):
    total = 0
    for num in numsList:
        total += num
    avg = total / len(numsList)
    return avg

# Display the results with formating the avg to two decimal points
def displayData(lo, hi, total, avg):
    print(LINE)
    print("The lowest number is:", lo)
    print("The highest number is:", hi)
    print("The total of the numbers is:", total)
    print(f"The average of the numbers is: {avg:.2f}")
    print(LINE) 
    
# calling the main function
main()