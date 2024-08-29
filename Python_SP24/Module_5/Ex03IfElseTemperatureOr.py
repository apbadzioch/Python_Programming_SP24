# If/Else Temperature Program Example with or operator

# Description:
# Have user enter a temperature. Based on that temperature, the program will print either Statement A or Statement B. 

# Hint: The or condition has two sub-expressions (temperature < 50), (temperature > 80).
# When using or, only ONE has to be true for the entire condition to be true! Try it out and enter
# a 50 for the temperature, and then try it again, and enter an 80 for the temperature. What happens?

# If you enter a 50, 50 will be stored in the variable temperature.
# Python first checks (temperature < 50).
# THIS IS FALSE. 50 is NOT less than 50.
# The value 50 is == (equal to) 50, or <= (less than or equal to) 50, but it is not simply <50

temperature = float(input("Enter temperature: "))
if (temperature < 50 or temperature > 80):
    print ("The temperature is a little extreme!")  #Statement A
else:
    print("The temperature is just right!")         #Statement B

# OUTPUT
'''
Enter temperature: 100
The temperature is a little extreme!
'''
