# break and continue statements
'''
DESCRIPTION:
Have the user enter points earned in a basket ball game
(make sure to validate the points entered are 1, 2, or 3)
continuously until the total is greater than or equal to 10
and display the total points.

EXAMPLE:
RUN1:
Enter points [1-3]: 1
Enter points [1-3]: 3
Enter points [1-3]: 2
Enter points [1-3]: 0
Invalid! Enter points [1-3]: -1
Invalid! Enter points [1-3]: 3
Enter points [1-3]: 3
Total points = 12

RUN2:
Enter points [1-3]: 3
Enter points [1-3]: 3
Enter points [1-3]: 3
Enter points [1-3]: 1
Total points = 10
'''

'''
total = 0
while total <= 10:
    points = int(input("Enter points [1-3]: "))
    if points >= 1 and points <= 3:
        total += points
    else:
        print("Invalid!", end = ' ')
print("Total points =", total)
'''

total = 0
flag = True
while flag:
    points = int(input("Enter points [1-3]: "))
    if points >= 1 and points <= 3:
        total += points
        if total < 10:
            continue
        else:
            break
    else:                               # else if (points < 1 or points > 3):
        print("Invalid!", end = ' ')
print("Total points =", total)
    








