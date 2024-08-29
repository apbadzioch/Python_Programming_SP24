# Example 7-9: Using append, insert, and extend methods with lists

names =[ 'Graham Chapman','Eric Idle','Terry Gilliam','Terry Jones','John Cleese','Michael Palin']

names.append('Dave Foley')
print(mpfc)
#['Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin', 'Dave Foley']

names.extend(['Bruce McCulloch','Kevin McDonald'])
print(mpfc)
#'Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin', 'Dave Foley', 'Bruce McCulloch', 'Kevin McDonald']

names.insert(len(mpfc), 'Mark McKinney')
print(mpfc)
#['Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin', 'Dave Foley', 'Bruce McCulloch', 'Kevin McDonald', 'Mark McKinney']

names.insert(0,'Scott Thompson')
print(mpfc)
#['Scott Thompson', 'Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin', 'Dave Foley', 'Bruce McCulloch', 'Kevin McDonald', 'Mark McKinney']


# OUTPUT
'''
['Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin', 'Dave Foley']
['Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin', 'Dave Foley', 'Bruce McCulloch', 'Kevin McDonald']
['Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin', 'Dave Foley', 'Bruce McCulloch', 'Kevin McDonald', 'Mark McKinney']
['Scott Thompson', 'Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin', 'Dave Foley', 'Bruce McCulloch', 'Kevin McDonald', 'Mark McKinney']
'''
