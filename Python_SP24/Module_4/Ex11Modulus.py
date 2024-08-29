# Example: Player's Height (Use of Modulus % Operator)
# Name: Enter your fullname here
# Description: If a baseketball player's height is 80 inches.
#                   Write a program to calculate and display the player's
#                   height in feet and inches

# Algorithm:
#    a. Declare int constant: INCHES_FEET_CONVERSION_FACTOR
#    b. Declare int variables: playerHeightInches, playerHeightFeet,
#                              playerHeightRemainingInches
#    c. Store 12 in INCHES_FEET_CONVERSION_FACTOR constant
#    d. Input playerHeightInches from user
#    e. Calculate playerHeightFeet as follows: playerHeightInches / INCHES_FEET_CONVERSION_FACTOR
#    f. Calculate playerHeightRemainingInches as follows: playerHeightInches % INCHES_FEET_CONVERSION_FACTOR
#    g. Display the results in the variables: playerHeightInches, playerHeightFeet, playerHeightRemainingInches with descriptive messages

INCHES_FEET_CONVERSION_FACTOR = 12;
playerHeightFeet = 0
playerHeightRemainingInches = 0

playerHeightInches = int(input("Enter player's height in inches: "))
playerHeightFeet = playerHeightInches // INCHES_FEET_CONVERSION_FACTOR;
playerHeightRemainingInches = playerHeightInches % INCHES_FEET_CONVERSION_FACTOR;

print("The basketball player's height in inches is =", playerHeightInches)
print("Which is", playerHeightFeet, "feet ")
print("        ", playerHeightRemainingInches, "inches")

# OUTPUT
'''
Enter player's height in inches: 61
The basketball player's height in inches is = 61
Which is 5 feet 
         1 inches
'''
