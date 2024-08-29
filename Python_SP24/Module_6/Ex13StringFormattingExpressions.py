# String formatting expressions

msg = 'Bright Side of Life'
print('Take a walk on the %s !' % msg)
# Displays: Take a walk on the Bright Side of Life !

i = 8675309
j = 'Integers:===%d===%-10d===%010d' % (i,i,i)
print(j)
# Displays: Integers:===8675309===8675309   ===0008675309

f = 8.675309
j = 'Floats: %e | %f | %g' % (f,f,f)
print(j)
# Displays: Floats: 8.675309e+00 | 8.675309 | 8.67531

# OUTPUT
'''
Take a walk on the Bright Side of Life !
Integers:===8675309===8675309   ===0008675309
Floats: 8.675309e+00 | 8.675309 | 8.67531
'''
