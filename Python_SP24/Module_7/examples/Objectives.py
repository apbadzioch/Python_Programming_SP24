# TOPICS
'''
- while loop
  -- program controlled while loop (predetermined iterations of the loop) 
  -- user controlled while loop (user determines the iterations of the loop)
  -- sentinel controlled while loop (similar to user controlled but with an input value to signify end of loop)
'''

'''
# Need for loops/iterations
# print your name 1, 5 times
print("Suma Rao")
print("Suma Rao")
print("Suma Rao")
print("Suma Rao")
print("Suma Rao")
'''

#  -- program controlled while loop (predetermined iterations of the loop)
# print your name 50 times or more...
'''
count = 0                # initialization statement (initValue is = 0)
#if count < 50:
while count < 50:        # testing condition (endValue is = 50)
    print("Suma Rao")
    count += 1           # update statement (control the loop/iterations)
'''

#  -- user controlled while loop (user determines the iterations of the loop)
'''
Print multiples of 10 from 0 to until the end value entered by the user
for example:
Enter the end value: 100
0 10 20 30 40 50 60 70 80 90 100
'''
'''
count = 0
endValue = int(input("Enter the end value: "))
while count <= endValue:        
    print(count, end = ' ')
    count += 10
'''

#  -- sentinel controlled while loop (similar to user controlled but with an input value to signify end of loop)
'''
Keep reading values until the input is 0 and display the sum of the numbers entered
For example:
Enter a number to add [enter 0 to STOP]: 5
Enter a number to add [enter 0 to STOP]: 5
Enter a number to add [enter 0 to STOP]: 10
Enter a number to add [enter 0 to STOP]: 100
Enter a number to add [enter 0 to STOP]: 1
Enter a number to add [enter 0 to STOP]: 0
Sum of numbers entered = 121
'''
sentinel = int(input("Enter a number to add [enter 0 to STOP]: "))
sum = 0
while sentinel != 0:        
    sum += sentinel
    sentinel = int(input("Enter a number to add [enter 0 to STOP]: "))
print("Sum of numbers entered =", sum)
