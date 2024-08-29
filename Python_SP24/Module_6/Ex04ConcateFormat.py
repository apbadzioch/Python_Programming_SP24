# This program asks the user to enter a food bill amount,
# and the program then calculates the tip (18%) and tax (7%) and final total.
# The program uses concatenate and decimal formatting to produce answers set to 2 decimal places.

# Declare variables for food charges, tip, tax, and total.
food = 0.0
tip = 0.0
tax = 0.0
total = 0.0

# Constants for the tax rate and tip rate.
TAX_RATE = 0.07
TIP_RATE = 0.18

# Get the food charges.
food = float(input("Enter the charge for food: "))

# Calculate the tip.
tip = food * TIP_RATE

# Calculate the tax.
tax = food * TAX_RATE

# Calculate the total.
total = food + tip + tax

# Print the tip, tax, and total.
print ("Tip: $" + format(tip, '.2f'))
print ("Tax: $" + format(tax, '.2f'))
print ("Total: $" + format(total, '.2f'))

# OUTPUT
'''
Enter the charge for food: 20
Tip: $3.60
Tax: $1.40
Total: $25.00
'''
