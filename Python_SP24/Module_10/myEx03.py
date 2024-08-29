'''
Traversing Lists
Splitting string to list
shifting list
'''

# create a string with all the list functions seperateed by space and using split function print each of the elements in the list
strFuncNamesBySpace = "len min max sum random.shuffle"
lstFuncNamesBySpace = strFuncNamesBySpace.split(' ')
print(lstFuncNamesBySpace)
for i in lstFuncNamesBySpace:
    print(i, end=' ')
print()
print()

# create a string with all the list functions seperated by , and using split function print each of the elements in the list
strFuncNamesByComma = "len, min, max, sum, random.shuffle"
lstFuncNamesByComma = strFuncNamesByComma.split(', ')
for i in lstFuncNamesByComma:
    print(i, end=' ')
print()
print()

# create a string with todays date in MM/DD/YYYY format and using split function print as MM DD YYYY
strDate = "04/16/2024"
lstDate = strDate.split('/')
for i in lstDate:
    print(i, end=' ')
print()
print()

# shifting left functions list
lst = [] + lstFuncNamesByComma
print('new list:', lst)
temp = lst[0]
for i in range(1, len(lst)):
    lst[i - 1] = lst[i]
lst[-1] = temp
print('after shifting left')
for i in lst:
    print(i, end=' ')
print()
print()

# shifting right functions list
lst = [] + lstFuncNamesBySpace
print('new list:', lst)
temp = lst[-1]
for i in range(len(lst)-1, 0, -1):
    lst[i] = lst[i - 1]
lst[0] = temp
print('after shfting right')
for i in lst:
    print(i, end=' ')
print()
print()

# shifting left date list using slicing
dlst = lstDate[1:] + lstDate[:1]
print('after shifting left using slicing')
for i in dlst:
    print(i, end=' ')
print()
print()

# shifting right date list
dlst = lstDate[-1:] + lstDate[:-1]
print('after shifting right using slicing')
for i in dlst:
    print(i, end=' ')
print()
print()