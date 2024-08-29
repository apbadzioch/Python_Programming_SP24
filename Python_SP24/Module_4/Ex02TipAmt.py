# Program to calculate the tip amount.

# Declare variables for food charges, tip
food = 0.0
tip = 0.0

# Constants for the tip rate
TIP_RATE = 0.20

# Get the food charges
food = float(input("Enter the charge for food: "))

# Calculate the tip
tip = food * TIP_RATE

# Print the tip
print ("Tip =", tip)

#OUTPUT
'''
Enter the charge for food: 20
Tip = 4.0
'''
