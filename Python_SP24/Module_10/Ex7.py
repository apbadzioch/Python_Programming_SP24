# Sorting lists: Selection Sort
'''
Append randomly generated 6 lotto numbers in the range 1-54 to a list
Print the numbers generated in the list
Sort the numbers ascending using selection sort 
Print the sorted numbers
Clear the list
Append randomly generated 6 lotto numbers in the range 1-54 to a list again
Print the numbers generated in the list
Sort the numbers descending using selection sort 
Print the sorted numbers
Modularize the program using functions

# Example
Original List: [53, 4, 52, 38, 48, 39]
Pass #1: [53, 4, 52, 38, 48, 39]
Pass #2: [4, 53, 52, 38, 48, 39]
Pass #3: [4, 38, 52, 53, 48, 39]
Pass #4: [4, 38, 39, 53, 48, 52]
Pass #5: [4, 38, 39, 48, 53, 52]
Pass #6: [4, 38, 39, 48, 52, 53]
List after sort: [4, 38, 39, 48, 52, 53]
Lowest = 4
Highest = 53
'''
import random
def populateList(lst):
    for i in range(6):
        lst.append(random.randint(1, 54))

def selectionSort(lst):
    # traverse the list
    for i in range(len(lst)):
        # find the lowest
        loIndex = i
        for j in range (i+1, len(lst)):
            if lst[j] < lst[loIndex]:
                loIndex = j
        print("Pass #" + str(i+1) + ":", lst)
        # swap the found lowest element with the first element
        lst[i], lst[loIndex] = lst[loIndex], lst[i]
        
def main():
    lst = []
    populateList(lst)
    print("Original List:", end = ' ')
    print(lst)

    selectionSort(lst)
    print("List after ascending sort:", end = ' ')
    print(lst)

    print("Lowest =", lst[0])
    print("Highest =", lst[-1])
    
main()

# output
'''
Original List: [53, 4, 27, 38, 54, 5]
Pass #1: [53, 4, 27, 38, 54, 5]
Pass #2: [4, 53, 27, 38, 54, 5]
Pass #3: [4, 5, 27, 38, 54, 53]
Pass #4: [4, 5, 27, 38, 54, 53]
Pass #5: [4, 5, 27, 38, 54, 53]
Pass #6: [4, 5, 27, 38, 53, 54]
List after ascending sort: [4, 5, 27, 38, 53, 54]
Lowest = 4
Highest = 54
'''
