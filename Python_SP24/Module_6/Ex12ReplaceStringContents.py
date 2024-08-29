# Replace string contents

lunch = 'SPAM SPAM SPAM'
print(lunch)

dinner = lunch.replace('SPAM','Steak')
print(dinner)

midnightsnack = dinner.replace('Steak', 'Hamburger', 1)
print(midnightsnack)

# OUTPUT
'''
SPAM SPAM SPAM
Steak Steak Steak
Hamburger Steak Steak
'''
