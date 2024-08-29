# If/Else Temperature Program with and operator (Example 2)

# Description:

# Have user enter a temperature.
# Based on that temperature, the program will print either Statements A/B or Statement C. 

temperature = float(input("Enter temperature: "))
if (temperature >= 50 and temperature < 80):
    print ("The temperature is just right!")         #Statement A
    print ("I love this weather!")                   #Statement B
else:
    print("The temperature is a little extreme!")    #Statement C
    
# OUTPUT
# TEST RUN 1
'''
Enter temperature: 50
The temperature is just right!
I love this weather!
'''
# TEST RUN 2
'''
Enter temperature: 80
The temperature is a little extreme!
'''
