# TOPICS
'''
- for loop (counter controlled loops)
  -- range(endValue)
  -- range(startValue, endValue)
  -- range(startValue, endValue, step)
'''

LINE = '*~' * 20

#  -- range(endValue) 
# print your name 10 times can be one of the following

'''
for i in range(10):
    print("Suma Rao")
print("i =", i)
print(LINE)

# using while loop 
i = 0
while i < 10:
    print("Suma Rao")
    i += 1
print("i =", i)
print(LINE)
'''

# -- range(startValue, endValue)
# print numbers horizontally with a space in between starting from 10 to 20
# 10 11 12 ... 20
'''
for i in range(10, 21):
    print(i, end = ' ')
print()
print(LINE)

i = 10
while i < 21:
    print(i, end = ' ')
    i += 1
print()
print(LINE)
'''
# -- range(startValue, endValue, step)
'''
Print multiples of 10 from 0 to until the end value entered by the user
for example:
Enter the end value: 100
0 10 20 30 40 50 60 70 80 90 100
'''
endValue = int(input("Enter the end value: "))
for i in range(0, endValue+1, 10):
    print(i, end = ' ')
print()
print(LINE)    

endValue = int(input("Enter the end value: "))
i = 0
while i < endValue+1:
    print(i, end = ' ')
    i += 10
print()
print(LINE) 














