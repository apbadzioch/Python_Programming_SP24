# if statement example
# Description:
# Have user enter an age.
#    If the age is less than 21 (that means, 20 or lower) then Statement A and Statement B will be executed.
#    If the age is 21 or higher, than Statements A/B are NOT executed.
#    Regardless of the age, Line 4 will always be executed since it is not part of the if. 
#    Notice the indentation.

age = int(input("Enter age: "))
if (age < 21):
    print ("You cannot buy a drink!")  #Statement A
    print ("You must be 21!")          #Statement B
print("Bye")                           # Line 4


# OUTPUT

# TEST RUN1
'''
Enter age: 20
You cannot buy a drink!
You must be 21!
Bye
'''

# TEST RUN2
'''
Enter age: 21
Bye
'''
