# using len function

p = input("What is the password? ")
lp = len(p)
if lp < 8 or lp >15:
    print("Password", p, "is not between 8 and 15 characters")
else:
        print("Password", p, "is between 8 and 15 characters")

# OUTPUT
# TEST RUN 1
'''
What is the password? 1234
Password 1234 is not between 8 and 15 characters
'''

# TEST RUN 2
'''
What is the password? SKDJF9385
Password SKDJF9385 is between 8 and 15 characters
'''
