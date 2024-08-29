# Calculate area of a circle and format and display to 2 decimal places

PI = 3.1415
area = 0.0    # Set to 0 for now so we know it will hold a decimal
radius = float(input("Enter radius: "))

area = PI * radius * radius
print("Area = ", format(area,'.2f'))

#OUTPUT
'''
Enter radius: 10
Area =  314.15
'''
