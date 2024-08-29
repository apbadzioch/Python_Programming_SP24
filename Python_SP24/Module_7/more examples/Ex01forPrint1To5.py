# Description: Lists numbers 0,1,2,3,4 vertically using for loop in 2 different ways

LINE='-----------------------------------'
for num in [0, 1, 2, 3, 4]:
     print(num)
print(LINE)

# Same as loop above but uses range
for num in range(5):
     print(num)
print(LINE)

# This is a new one
# We will print out the numbers
# and then sum them up
num=0
sum=0
for num in range(5):
     sum = sum + num
print("Sum =", sum)
        
# OUTPUT
'''
0
1
2
3
4
-----------------------------------
0
1
2
3
4
-----------------------------------
Sum = 10
'''
