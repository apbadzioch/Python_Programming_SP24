# Program to find the total number of bugs collected

# Initialize variables for bugs and
# total number of bugs collected.
bugs = 0
total = 0

# Get number of bugs collected each day
for day in range(5):
    bugs = int(input('Enter the number of bugs collected today: '))
    total += bugs

# Display the total number of bugs collected.
print ('Total bugs collected: ', total)

# OUTPUT
'''
Enter the number of bugs collected today: 5
Enter the number of bugs collected today: 5
Enter the number of bugs collected today: 5
Enter the number of bugs collected today: 5
Enter the number of bugs collected today: 5
Total bugs collected:  25
'''
