# Example 7-4: del and remove functions

names =['Scott Thompson', 'Graham Chapman', 'Eric Idle',
            'Terry Gilliam', 'Terry Jones', 'John Cleese']

LINE='--------------------------------------------------------------------------------'
print(names)
print(LINE)

del(names [-2:])
print(names)
print(LINE)

names.remove('Scott Thompson') 
print(names)
print(LINE)

# OUTPUT
'''
['Scott Thompson', 'Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese']
--------------------------------------------------------------------------------
['Scott Thompson', 'Graham Chapman', 'Eric Idle', 'Terry Gilliam']
--------------------------------------------------------------------------------
['Graham Chapman', 'Eric Idle', 'Terry Gilliam']
--------------------------------------------------------------------------------
'''
