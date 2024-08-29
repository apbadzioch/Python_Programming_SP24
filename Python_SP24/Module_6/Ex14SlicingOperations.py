# Slicing operations

m = "Monty Python's The Meaning of Life"
n = m[:]
print(m[0:5])   # Monty
print(m[15:])   # The Meaning of Life
print(m[:14])   # Monty Python's
print(m[:-7])   # Monty Python's The Meaning
print(m[-4:])   # Life
print(n)        # Monty Python's The Meaning of Life

# OUTPUT
'''
Monty
The Meaning of Life
Monty Python's
Monty Python's The Meaning 
Life
Monty Python's The Meaning of Life
'''
