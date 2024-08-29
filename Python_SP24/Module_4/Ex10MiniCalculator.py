# Example: Mini Calculator
# Name: Enter your fullname here
# Description: Input two numbers and display the sum, difference, product,
#                    quotient, and remainder of the two numbers.

# Algorithm:
#    a. Declare character constants: ADDITION_OP, SUBTRACTION_OP, MULTIPLICATION_OP, DIVISON_OP, REMAINDER_OP, ASSIGNMENT_OP
#    b. Declare int variables: number1, number2, sum, diff, prod, quot, rem
#    c. Store the following characters: 
#       + in ADDITION_OP constant
#       - in SUBTRACTION_OP constant
#       * in MULTIPLICATION_OP constant
#       / in DIVISON_OP constant
#       % in REMAINDER_OP constant
#       = in ASSIGNMENT_OP constant
#    d. Input number1 from user
#    e. Input number2 from user
#    f. Calculate sum as follows: sum = number1 + number2;
#    g. Calculate diff as follows: diff = number1 - number2;
#    h. Calculate prod as follows: prod = number1 * number2;
#    i. Calculate quot as follows: quot = number1 / number2;
#    j. Calculate remainder as follows: rem = number1 % number2;
#    k. Display the results in the variables: num1, num2, sum, diff, prod, quot, rem with descriptive messages

# Create constants strings
ADDITION_OP = '+';
SUBTRACTION_OP = '-';
MULTIPLICATION_OP = '*';
DIVISON_OP = '/';
REMAINDER_OP = '%';
ASSIGNMENT_OP = '=';

# Input two numbers from user
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

# Keep answers as integers (except division)
sum = 0
diff = 0
prod = 0    
quot = 0.0    # Division usually ends up with a decimal
remainder = 0

sum = number1 + number2
diff = number1 - number2
prod = number1 * number2
quot = number1 / number2
rem = number1 % number2

print(number1, ADDITION_OP, number2, ASSIGNMENT_OP, sum)
print(number1, SUBTRACTION_OP, number2, ASSIGNMENT_OP, diff)
print(number1, MULTIPLICATION_OP, number2, ASSIGNMENT_OP, prod)
print(number1, DIVISON_OP, number2, ASSIGNMENT_OP, format(quot,'.2f'))
print(number1, REMAINDER_OP, number2, ASSIGNMENT_OP, rem)

# OUTPUT
'''
Enter number 1: 10
Enter number 2: 3
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
10 % 3 = 1
'''
