# Calculate tip amount and use concatenate, str, and format to print

# Declare variables for food charges, tip
food = 0.0
tip = 0.0

# Constants for the tip rate
TIP_RATE = 0.20

# Get the food charges
food = float(input("Enter the charge for food: "))

# Calculate the tip
tip = food * TIP_RATE
print ("Tip: $" + str(tip))

# Now use format to make sure it prints 2 decimal places
print ("Tip: $" + format(tip, '.2f'))

# OUTPUT
'''
Enter the charge for food: 20
Tip: $4.0
Tip: $4.00
'''
