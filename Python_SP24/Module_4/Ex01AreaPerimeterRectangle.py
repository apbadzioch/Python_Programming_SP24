# Name: Enter your fullname here
# Lab: Sample - Area & Perimeter of a Rectangle
# Description: This program calculates the area and perimeter 
#                of a rectangle, based on inputted length and width

# Algorithm:
# Get: length
# Get: width
# Set: perimeter = 2 * (length + width)
# Set: area = length * width
# Display: perimeter and area

length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
area = length * width
print("Area = ", area)
print("Perimeter = ", perimeter)

# OUTPUT
'''
Enter length: 10
Enter width: 5
Area =  50.0
Perimeter =  30.0
'''
