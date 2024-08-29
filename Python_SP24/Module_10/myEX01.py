# List Topics

'''
Creating Lists
Indexing Lists
Copying Lists
Slicing Lists
List Operators: +, *, and in/not
List Functions: len, min, max, sum, random.shuffle
'''

import random

# create and print a 3-element tests list and initialize with test values
tests = [88.8, 99.9, 100]
print("test list", tests)

# using Indexing print the first element in the test lists
print("first element:", tests[0])

# using Indexing print the last element in the test lists
print("last element:", tests[-1])

# - OR - 
print("last element:", tests[len(tests)-1])
print("second to last element:", tests[len(tests)-2])

# create 3-element list and intialize with 0
quizzes = [0] * 3

# compare test and quizzes list
if tests == quizzes:
    print("tests and quizzes are equal")
elif tests < quizzes:
    print("tests are greater than quizzes")
else:
    print("tests are lesser than quizzes")

# copy test list to quizzes list using assignment op (reference is made)
quizzes = tests
print("quizzes list using referencing:", quizzes)
tests[0] = 100
print("tests list:", tests)
print("quizzes list:", quizzes)

# make a duplicate copy of quizzes list to test list
quizzes = [] + tests
print("quizzes list using duplicate copy:", quizzes)
tests[0] = 88.8
print("tests list:", tests)
print("quizzes list:", quizzes)
quizzes[0] = 88.8
print("quizzes list:", quizzes)

# compoare lists again
if tests == quizzes:
    print("tests and quizzes are equal")
elif tests < quizzes:
    print("tests are greater than quizzes")
else:
    print("tests are lesser than quizzes")

# concatenate both lists to totalList
totalList = tests + quizzes
print("totalList:", totalList)

# assign 100 to the last element in totalList
print("last element in totalList:", totalList[-1])

# - OR - 
print("last element in totalList:", totalList[len(totalList)-1])

# traverse the list and find if 100 exists
if 100 in totalList:
    print("100 exists in totalList")
else:
    print("100 diesn't exist in totalList")

# using Slicing to print the first 3 elements in the list
print("first 3 elements in totalList:", totalList[:3])

# using Slicing to print the last 3 elements in the list
print("last 3 elements in totalList:", totalList[-3:])

# using Slicing to print every alternate element in the list
print("alternate elements in totalList", totalList[::2])

# randomly shuffle list
random.shuffle(totalList)
print("totalList", totalList)

# find the len, min, max, sum, avg of totalList
print("length", len(totalList))
print("mininum", min(totalList))
print("maximum", max(totalList))
print("sum", sum(totalList))
print("average", sum(totalList)/len(totalList))
