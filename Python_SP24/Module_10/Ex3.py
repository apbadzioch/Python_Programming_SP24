'''
Traversing lists
Splitting string to list
Shifting lists
'''
# create a string with all the list functions separated by space and using split function print each of the element in the list
strFuncNamesBySpace = "len min max sum random.shuffle"
lstFuncNamesBySpace = strFuncNamesBySpace.split(' ')
#print(lstFuncNamesBySpace)
for i in lstFuncNamesBySpace:
    print(i, end = ' ')
print()
print()

# create a string with all the list functions separated by , and using split function print each of the element in the list
strFuncNamesByComma = "len, min, max, sum, random.shuffle"
lstFuncNamesByComma = strFuncNamesByComma.split(', ')
for i in lstFuncNamesByComma:
    print(i, end = ' ')
print()
print()

# create a string with today's date in MM/DD/YYYY format and using split function print as MM DD YYYY
strDate = "03/04/2024"
lstDate = strDate.split('/')
for i in lstDate:
    print(i, end = ' ')
print()
print()

# Shifting left functions list
lst = [] + lstFuncNamesByComma
print("new lst =", lst)

temp = lst[0]
for i in range(1, len(lst)):
    lst[i-1] = lst[i]
lst[-1] = temp

print("After shifting left")
for i in lst:
    print(i, end = ' ')
print()
print()
    
# Shifting right functions list
lst = [] + lstFuncNamesBySpace
print("new lst =", lst)

temp = lst[-1]
for i in range(len(lst)-1, 0, -1):
    lst[i] = lst[i-1]
lst[0] = temp

print("After shifting right")
for i in lst:
    print(i, end = ' ')
print()
print()

# Shifting left date list using slicing
dlst = lstDate[1:] + lstDate[:1]

print("After shifting left using slicing")
for i in dlst:
    print(i, end = ' ')
print()
print()

# Shifting right date list using slicing
dlst = lstDate[-1:] + lstDate[:-1]

print("After shifting right using slicing")
for i in dlst:
    print(i, end = ' ')
print()
print()

# OUTPUT
'''
len min max sum random.shuffle 

len min max sum random.shuffle 

03 04 2024 

new lst = ['len', 'min', 'max', 'sum', 'random.shuffle']
After shifting left
min max sum random.shuffle len 

new lst = ['len', 'min', 'max', 'sum', 'random.shuffle']
After shifting right
random.shuffle len min max sum 

After shifting left using slicing
04 2024 03 

After shifting right using slicing
2024 03 04 
'''

