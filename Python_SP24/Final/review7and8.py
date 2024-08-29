'''
# sum and avg the items in a list 1-7
#lst = [1, 2, 3, 4, 5, 6, 7]
lst = [i for i in range(1, 8)]
print(lst)

t = 0
for e in lst:
    t += e
print("Sum", t)

a = t/len(lst)
print("Avg", a)
'''

'''
# send a list as function arguments to find the sum and avg
def findSum(lst):
    t = 0
    for e in lst:
       t += e
    return t

def displayAvg(t, s):
    print("Avg", t/s)
    
def main():
    lst = [i for i in range(1, 8)]
    t = findSum(lst)
    print("Sum", t)
    displayAvg(t, len(lst))
    
main()
'''

'''
# print list elements in reverse order
def printReverse(lst):
    print(lst[::-1])
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end='')
    print()
    
lst = list("python")
print(lst)
printReverse(lst)
'''

'''
# define a function to find if a string is a palindrome
def findPalindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False
    
def main():
    print(findPalindrome("Noon"))
    print(findPalindrome("RADAr"))
    print(findPalindrome("suma"))
   
main()
'''

'''
# define a 2d list of 3x4 with all 0s
#lst2d = [[0]*4, [0]*4, [0]*4]
lst2d = [[0]*4 for i in range(3)]
print(lst2d)
'''

# randomly fill a 2x3 2d list with random numbers 1-9
import random
rand2d = [[0]*3 for i in range(2)]

for r in range(2):
    for c in range(3):
        rand2d[r][c] = random.randint(1, 9)

print(rand2d)
print("first elem", rand2d[0][0])
print("last elem", rand2d[-1][-1])
print("first row second elem", rand2d[0][1])
