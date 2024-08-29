# nested loops

'''
Have the user enter 2 inputs: any character and in how many rows
and display it in the following patterns using nested loops.

For example:
Enter a character to print: *
In how many rows? 4
*
**
***
****
****
***
**
*
'''

sym = input("Enter a character to print: ")
rows = int(input("In how many rows? "))

for r in range(1, rows+1):
    for c in range(1, r+1):     # for c in range(r): can also be used
        print(sym, end = '')
    print()

for r in range(rows, 0, -1):
    for c in range(1, r+1):     # for c in range(r): can also be used
        print(sym, end = '')
    print()
