# Testing string contents

x = input("Please type in a string of Upper Case Alpha Characters: ")
if x.isalpha() and x.isupper():
    print("You may pass!")
else:
    print("Off to the volcano!")

# OUTPUT
# TEST RUN 1
'''
Please type in a string of Upper Case Alpha Characters: HELLO
You may pass!
'''
# TEST RUN 2
'''
Please type in a string of Upper Case Alpha Characters: 12345
Off to the volcano!
'''

# TEST RUN 3
'''
Please type in a string of Upper Case Alpha Characters: hello
Off to the volcano!
'''
