# Topics
'''
- read strings from the keyboard
- in and not in Operators
- Comparing strings
- String Functions: len, max, min
'''

# program description
'''
Receive the user's full name and find the length, max and min characters in the name.
Have the user enter a character/string to search and display if string exists in his/her name.
Compare user's name with the search string and print appropriate messages.
'''

name = input("enter your name: ")
print("17", len(name))
print("18", max(name))
print("19", min(name))

getStr = input("what are you searching for? ")

if getStr in name:
    print(getStr, "exists in", name)
else:
    print(getStr, "does not exists in", name)
    
name2 = input("enter another name: ")

if name < name2:
    print(name, name2)
else:
    print(name2, name)
    







