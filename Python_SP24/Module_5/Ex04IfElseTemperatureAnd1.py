# If/Else Temperature Program Example with and operator

# Description:
# Have user enter a temperature. Based on that temperature, the program will print either Statement A or Statement B. 

# Hint: The and condition has two sub-expressions (temperature >= 50), (temperature < 80).
# When using and, BOTH sub-expressions have to be true for the entire condition to be true!
# Try it out and enter a 50 for the temperature, and then try it again,
# and enter an 80 for the temperature. What happens?

# If you enter a 50, 50 will be stored in the variable temperature.
# Python first checks (temperature >= 50).  THIS IS TRUE.
# Then it checks to make sure that (temperature < 80).
# This is also true, so entire condition is TRUE and Statement A is executed.

# Run it again and enter an 80. The value 80 will be stored in the variable temperature.
# Python first checks (temperature >= 50).  THIS IS TRUE.
# Then it checks to make sure that (temperature < 80).
# This is NOT true, so entire condition is FALSE and Statement B is executed.

temperature = float(input("Enter temperature: "))
if (temperature >= 50 and temperature < 80):
    print ("The temperature is just right!")         #Statement A
else:
    print("The temperature is a little extreme!")    #Statement B
    
# OUTPUT
'''
Enter temperature: 50
The temperature is just right!
'''
