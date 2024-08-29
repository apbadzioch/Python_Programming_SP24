# List Topics
'''
Creating lists
Indexing lists
Comparing lists
Copying lists
Slicing lists
List operators: +, *, and in/not
List functions: len, min, max, sum, random.shuffle
'''
import random

# create and print a 3-element tests list and initialize with test values
tests = [88.8, 99.9, 100]
print("tests list", tests)

# Using Indexing print the first element in the tests list
print("first element in the tests list", tests[0])

# Using Indexing print the last element in the tests list
print("last element in the tests list", tests[-1])

# - OR-
print("last element in the tests list", tests[len(tests)-1])
print("second to last element in the tests list", tests[-2])
      
# Create 3-element quizzes list and initialize with 0
quizzes = [0] * 3

# Compare tests and quizzes list
if tests == quizzes:
    print("tests and quizzes lists are equal")
elif tests > quizzes:
    print("tests list is greater than quizzes")
else:
    print("tests list is lesser than quizzes")    
   
# Copy tests list to quizzes list using assignment op (reference is made)
quizzes = tests
print("quizzes list using referencing", quizzes)
tests[0] = 100
print("tests list", tests)
print("quizzes list", quizzes)

# make a duplicate copy of quizzes list from tests list
quizzes = [] + tests
print("quizzes list using duplicate copy", quizzes)
tests[0] = 88.8
print("tests list", tests)
print("quizzes list", quizzes)
quizzes[0] = 88.8
print("quizzes list", quizzes)

# Compare tests and quizzes list again
if tests == quizzes:
    print("tests and quizzes lists are equal")
elif tests > quizzes:
    print("tests list is greater than quizzes")
else:
    print("tests list is lesser than quizzes")
    
# Concatenate tests and quizzes list to totalList
totalList = tests + quizzes
print("totalList", totalList)

# Assign 100 to the last element of totalList
print("last element in the totalList", totalList[-1])

# -OR-
print("last element in the totalList", totalList[len(totalList)-1])

# Traverse the list and find if 100 exists in totalList
if 100 in totalList:
    print("100 exists in totalList")
else:
    print("100 does exists in totalList")
    
# Using slicing print first 3 elements in the totalList
print("first 3 elements in the totalList", totalList[:3])

# Using slicing print last 3 elements in the totalList
print("last 3 elements in the totalList", totalList[-3:])

# Using slicing print every alternate element in the totalList
print("alternate element in the totalList", totalList[::2])

# Randomly shuffle totalList
random.shuffle(totalList)
print("totalList", totalList)

# Find the len, min, max, sum, and avg of totalList
print("len", len(totalList))
print("min", min(totalList))
print("max", max(totalList))
print("sum", sum(totalList))
print("avg", sum(totalList)/len(totalList))

# OUTPUT
'''
tests list [88.8, 99.9, 100]
first element in the tests list 88.8
last element in the tests list 100
last element in the tests list 100
second to last element in the tests list 99.9
tests list is greater than quizzes
quizzes list using referencing [88.8, 99.9, 100]
tests list [100, 99.9, 100]
quizzes list [100, 99.9, 100]
quizzes list using duplicate copy [100, 99.9, 100]
tests list [88.8, 99.9, 100]
quizzes list [100, 99.9, 100]
quizzes list [88.8, 99.9, 100]
tests and quizzes lists are equal
totalList [88.8, 99.9, 100, 88.8, 99.9, 100]
last element in the totalList 100
last element in the totalList 100
100 exists in totalList
first 3 elements in the totalList [88.8, 99.9, 100]
last 3 elements in the totalList [88.8, 99.9, 100]
alternate element in the totalList [88.8, 100, 99.9]
totalList [88.8, 88.8, 100, 99.9, 99.9, 100]
len 6
min 88.8
max 100
sum 577.4
avg 96.23333333333333
'''


