# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user
# to enter the total square feet in a tract of land and calculates the number of acres in the tract.
# Hint: Divide the amount entered by 43, 560 to get the number of acres.

# Variables to hold the size of the tract and number of acres.
tractSize = 0.0
acres = 0.0

# Constant for the number of square feet in an acre.
SQ_FEET_PER_ACRE = 43560

# Get the square feet in the tract.
tractSize = input("Enter the number of square feet in the tract: ")

# Calculate the acreage.
acres = float(tractSize) / SQ_FEET_PER_ACRE

# Print the number of acres.
print ("The size of that tract is", acres, "acres.")
print ("The size of that tract is", round(acres, 3), "acres.")
print ("The size of that tract is", round(acres, 2), "acres.")
print ("The size of that tract is", round(acres, 1), "acres.")
print ("The size of that tract is", round(acres), "acres.")

# OUTPUT
'''
Enter the number of square feet in the tract: 100000
The size of that tract is 2.295684113865932 acres.
The size of that tract is 2.296 acres.
The size of that tract is 2.3 acres.
The size of that tract is 2.3 acres.
The size of that tract is 2 acres.
'''
