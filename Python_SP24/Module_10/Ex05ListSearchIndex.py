# Example 7-5: Searching through list using index function

eatsteak =['Eat', 'steak', 'eat', 'steak', 'eat', 'a', 'big', 'ol', 'steer', 'Eat', 'steak', 'eat', 'steak', 'do', 'we', 'have', 'one', 'dear?']
print('The first occurence of steak is found at position', eatsteak.index('steak')) # Position 1
print('steak between indexes 7 and 10 is found at', eatsteak.index('steak',7, 11)) # Position 10

# OUTPUT
'''
The first occurence of steak is found at position 1
steak between indexes 7 and 10 is found at 10
'''
