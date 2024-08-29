# Topics
'''
- ASCII: Decimal Code (0-9: 48-57, A-Z: 65-90, and a-z: 97-122)
- ord and chr functions
- process strings and characters (single, double, and triple quotes)
- special characters using the escape sequence
- print function with the end argument
- str function
- Concatenation (+) and Repetition (*) Operators 
- read strings from the keyboard
'''

# program description
'''
Receive the user's course letter grade and display it's ASCII value as follows
using escape sequence where needed:

For example:
Enter your letter grade: A
"Your course letter grade is 'A' which corresponds to "ASCII" value 65"
which corresponds to "ASCII" value 65
which corresponds to 'ASCII' value 65
'''
LINE1= '---------------------------'
LINE = '~*' * 20

print(LINE)

lg = input("Enter your grade: ")
print('Your course letter grade is \'' + lg + "'", end=' ')
print("which corresponds to \"ASCII\" value", ord(lg))
print('which corresponds to "ASCII" value', ord(lg))
print('''which corresponds to 'ASCII' value ''' + str(ord(lg)))







