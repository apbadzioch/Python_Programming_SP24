# Write a program that asks the user to enter inches
# and then the program converts the inches into feet.
# HINT: 1 foot is equivalent to 12 inches.
# Divide the amount entered by 12 to get the number of feet

# Variables to hold feet and inches
# Assume they will all be integers
feet = 0
inches = 0
remainingInches = 0

# Constant for the inches to feet conversion
INCHES_PER_FEET = 12

# Get the inches
inches = int(input("Enter the number of inches: "))

# Calculate the feet with integer math
# EX: divide but get rid of the decimal
feet = inches // INCHES_PER_FEET

# Calculate leftover inches
# EX: long division and get remainder
remainingInches = inches % INCHES_PER_FEET

# Print the number of feet and number of inches
print (inches, "inches =", feet, "feet and", remainingInches, "inches")

#OUTPUT
'''
Enter the number of inches: 30
30 inches = 2 feet and 6 inches
'''
