# join and split methods

#Provide a grouping of strings. This grouping is called a
#tuple, and you will learn more about them later

mpfs = ('John Cleese','Terry Gilliam','Eric Idle','Terry Jones','Michael Palin','Graham Chapman')

# Provide a string to use as a connecter between objects in 
# the new joined string

delim = ' , '

#Do the join() and assign the new string to a variable. Print the original tuple and the new string

jmpfs = delim.join(mpfs)
print(mpfs)
# ('John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Graham Chapman')

print()
print(jmpfs)
# John Cleese , Terry Gilliam , Eric Idle , Terry Jones , Michael Palin , Graham Chapman

print()

# Split the joined string and return a list object
# containing the split-up strings. Assign that list object
# to a variable and print it out. You’ll learn more about
# list objects in a future module

smpfs = jmpfs.split(' , ')
print(smpfs)
# ['John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Graham Chapman']

# OUTPUT
'''
('John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Graham Chapman')

John Cleese , Terry Gilliam , Eric Idle , Terry Jones , Michael Palin , Graham Chapman

['John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Graham Chapman']
'''
