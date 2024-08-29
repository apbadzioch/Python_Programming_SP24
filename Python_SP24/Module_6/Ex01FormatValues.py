# Calculate and Format Circle Radius & Area

# Algorithm:
#   Set: radius to 10
#   Set: PI as a constant 
#   Calculate: area
#   Display: Display formatted radius and area

PI = 3.1415
radius = 10
area = 0.0    # Set to 0.0 for now so we know it will hold a decimal

area = PI * radius * radius
print("Area = ", area)

#############################################
# Below is a more advanced way to output the
# data using formatting.
#############################################

print("-----------------")
print("Radius = ", format(radius,'6.1f'))
print("Area = ", format(area,'8.1f'))

# OUTPUT
'''
Area =  314.15000000000003
-----------------
Radius =    10.0
Area =     314.2
'''
