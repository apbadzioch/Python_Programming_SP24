# This program asks the user to enter a food bill amount,
# and the program then calculates the tip (18%) and tax (7%) and final total.
# The program uses round function to display results.

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
print ("Tip =", tip)
print ("Tip =", round(tip, 3))
print ("Tax =", tax)
print ("Tax =", round(tax, 2))
print ("Total =", total)
print ("Total =", round(total))

#OUTPUT
'''
Enter the charge for food: 5
Tip = 0.8999999999999999
Tip = 0.9
Tax = 0.35000000000000003
Tax = 0.35
Total = 6.25
Total = 6
'''
