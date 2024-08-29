'''
3 + 4 * 4 > 5 * (4 + 3) – 1
3 + 16 > 5 * 7 - 1
19 > 35 - 1
19 > 34
False

2 * 2 - 3 > 2 and 5 >= 6
2 * 2 - 3 > 2 and False
False
'''

'''
print(3 + 4 * 4 > 5 * (4 + 3) - 1)
print(2 * 2 - 3 > 2 and 5 >= 6)
'''
'''
points = 1
match points:
    case 1: print("1 pointer")
    case 2: print("2 pointer")
    case 3: print("3 pointer")
    case _: print("invalid")

if points == 1:
    print("1 pointer")
elif points == 2:
    print("2 pointer")
elif points == 3:
    print("3 pointer")
else:
    print("invalid")
'''

'''
scores = 50
if scores >= 60:
    print("PASSED")
else:
    print("FAILED")

print("PASSED" if scores >= 60 else "FAILED")
'''

'''
print(0 if 10 % 3 == 0 else 1)
if 10 % 3 == 0:
    print(0)
else:
    print(1)
'''

'''
x = 2 if 2 > 3 else 3
print(x)

if 2 > 3:
    x = 2
else:
    x = 3
print(x)
'''

import random
print(random.randint(0, 5))










