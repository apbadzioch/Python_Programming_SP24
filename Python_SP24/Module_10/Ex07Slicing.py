# Example 7-7: Using slices to change lists

names =[ 'Graham Chapman','Eric Idle','Terry Gilliam','Terry Jones','John Cleese','Michael Palin']
names1 = names[:]		#Make a backup of the Flying Circus

names[0:2] = ['Scott Thompson', 'Dave Foley']
#Replace Graham and Eric with a couple of Kids

print(names)
#['Scott Thompson', 'Dave Foley', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin']

names[0:0]=names1[0:2]
#Add Graham and Eric back into the Circus. Keep the Kids

print(names)
#['Graham Chapman', 'Eric Idle', 'Scott Thompson', 'Dave Foley', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin']

names[2:4]=[]
#Release the Kids from their contract

print(names)
#['Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin']

# OUTPUT
'''
['Scott Thompson', 'Dave Foley', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin']
['Graham Chapman', 'Eric Idle', 'Scott Thompson', 'Dave Foley', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin']
['Graham Chapman', 'Eric Idle', 'Terry Gilliam', 'Terry Jones', 'John Cleese', 'Michael Palin']
'''
