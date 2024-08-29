# TOPICS
'''
- while loop
  -- program controlled while loop (predetermined iterations of the loop) 
  -- user controlled while loop (user determines the iterations of the loop)
  -- sentinel controlled while loop (similar to user controlled but with an input value to signify end of loop)
'''

# -- program controlled while loop (predetermined iterations of the loop) 
'''
# Need for loops/iterations
# print your name 5 times

print("Suma Rao")
print("Suma Rao")
print("Suma Rao")
print("Suma Rao")
print("Suma Rao")
'''
'''
i = 1                # initialization statement
while i <= 5:        # testing statement or condition to check
   print("Suma Rao")
   i += 1            # control statement that ends loop
'''

# -- user controlled while loop (user determines the iterations of the loop)
'''
Print multiples of 10 from 0 until the end value entered by the user
for example:
Enter the end value: 100
0 10 20 30 40 ... 100
'''
'''
endValue = int(input("Enter the end value: "))
i = 0            
while i <= endValue:        
   print(i, end = ' ')
   i += 10            
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

total = 0
num = int(input("Enter a number to add [enter 0 to STOP]: "))     # initialization statement
while num != 0:                                                   # 0 is the sentinal value and num != 0 is the testing condition
    total += num
    num = int(input("Enter a number to add [enter 0 to STOP]: ")) # control statement
print("Sum of numbers entered =", total)






