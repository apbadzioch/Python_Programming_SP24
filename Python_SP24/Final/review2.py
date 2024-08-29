'''
PEMDMAS - Parenthesis-1, Expnentiation (**)-2, [Multiplication (*), Divition (/, //),
            Modulus (%)-3], [Addition (+), Subtraction (-)-4], Associativity is left to right
5*2+3-8//3%4**2
5*2+3-8//3%16
10+3-8//3%16
10+3-2%16
10+3-2
13-2
11
'''

'''
print(5*2+3-8//3%4**2) # 11

a = 5
b = 10
print("Line 17:", a, b) # 5 10
a, b = b, a
print("Line 19:", a, b) # 10 5

a += b  # a = a + b, a = 10 + 5 = 15
print(a)        # 15

a = float(input("Enter a number: ")) # 4
a %= 5
print("a", a) # a 4.0

drinks = 5
pizza = 2
print(drinks + pizza)   # 7
print("drinks + pizza") # drinks + pizza
'''

'''
Valid/Invalid Identifiers:
1. phone_num: Valid (phoneNum, smallCaseCamelStyle), (PhoneNum, uppercaseCamelStyle)
2. phone#: Invalid (symbols not allowed)
3. phone num: Invalid (spaces not allowed)
4. phone123: Valid
5. _Phone: Valid
6. PHONE_NUM: valid (CONSTANTS we follow this style)
7. PI: valid
'''





















