# Random number generator program

# Description:

# The following will create a random number between 0 and 20. To create a random number
# between 1 and 10, change the (0,20) to (1,10). You must include the random library
# with the first import statement. Always put the import lines at the top of the program.

import random
radius = random.randint(0,20)
print("The radius is :", radius)
pi = 3.1415
area = pi * radius ** 2
print("Area : ", area)
        
# OUTPUT

# TEST RUN 1
'''
The radius is : 16
Area :  804.224
'''

# TEST RUN 2
'''
The radius is : 18
Area :  1017.846
'''
