# TOPIC: while loop
'''
Have the user enter the points made in a basket ball game and press y/Y
to continue entering points and when done entering points display the total points made.

For example:

Enter points made: 1
Do you want to continue? y
Enter points made: 2
Do you want to continue? Y
Enter points made: 3
Do you want to continue? Y
Enter points made: 3
Do you want to continue? y
Enter points made: 3
Do you want to continue? n

Total points made = 12
'''
repeat = 'y'
total = 0
#while repeat == 'y' or repeat == 'Y':
#while repeat.lower() == 'y':
while repeat.upper() == 'Y':
    points = int(input("Enter points made: "))
    total += points
    repeat = input("Do you want to continue? ")
print("\nTotal points made =", total)
