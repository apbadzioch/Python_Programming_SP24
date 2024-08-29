# Name: Enter your full name here
# Lab: Sample - Easy Calculate Circle Area
# Description: Set PI and input radius from user and calculate area

# Algorithm:
# Get: Radius
# Set: PI as a constant 
# Calculate: area
# Display: Message and area of circle

PI = 3.1415
area = 0.0    # Set to 0 for now so we know it will hold a decimal
radius = float(input("Enter radius: "))

area = PI * radius * radius
print("Area =", area)

# OUTPUT
'''
Enter radius: 4
Area = 50.264
'''
