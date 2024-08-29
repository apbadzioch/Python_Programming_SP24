# Topics
'''
- String methods:
    -- String methods to manipulate: islower, isupper, isalpha, isdigit, ialnum, isspace
    -- Searching substrings: find, rfind, endswith, startswith, count
    -- Converting strings: lower, upper, capitalize, title, swapcase, replace
    -- lstrip, rstrip, strip
'''

# program description
'''
1. 
Have the user enter 3 inputs: firstname, lastname, W-userid
If any left/right space entered strip the space
Then, create the user's email address using slicing as follows:
    first 4 characters of the firstname (with the first character in uppercase)
    first character of the lastname in uppercase
    last 3 characters of the W-userid
    followed by @hccs.edu
For example: if my firstname is suma, lastname is rao, and W-userid is W12345678
then, my email address is SumaR678@hccs.edu

2.
HINT: isalnum() isalpha() isdigit() with if statement
Then have the user enter a password.
Make sure the password entered matches the following rules:
    - at least 8 characters
        -- made of both alphabets and numbers
            --- with at least one alphabet and
            --- with at least one digit
'''

fname = input("enter first name: ").strip()
lname = input("enter last name: ")
wid = input("enter wid: ")

upperFirst = fname[0].upper()
newFname = upperFirst + fname[1:4]

uppperLast = lname[0].upper()

newWid = wid[-3:]

email = newFname+uppperLast+newWid+"@hccs.edu"
print(email)








