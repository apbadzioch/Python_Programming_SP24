'''
# function that prints the sum of numbers 1 to 5
def sum1to5():
    t = 0
    for i in range(1, 6):
        t += i
    print(t)
    
sum1to5()
'''

'''
# function to return lowest of 3 numbers passed as arguments
def findLowest(a, b, c):
    if a < b and a < c: low = a
    elif b < a and b < c: low = b
    else: low = c
    return low
    
def main():
    low = findLowest(11, 77, 5)
    print(low)
    print(findLowest(0, 77, 5))
    print(findLowest(11, 2, 5))

main()
'''

'''
# function to return true if the string argument has only alphas
def checkAlphabets(s):
    return s.isalpha()

def main():
    s = "helloHELLOhello hello"
    if checkAlphabets(s):
        print(s, "is only alphabets")
    else:
        print(s, "has more than alphas")
        
main()
'''

'''
# function to display true if the string argument has all lowercase characters
def displayLower(s):
    if s.islower():
        print(s, "is all lowercase")
    else:
        print(s, "is NOT all lowercase")

displayLower("hello")
displayLower("HELLO")
displayLower("Hello")
displayLower("hello!!")
'''

'''
# return number of uppercase and lowercase alphabets in a string argument
def countUpLow(s):
    l = u = 0
    for e in s:
        if e.islower():
            l += 1
        elif e.isupper():
            u += 1
    return l, u
            
print(countUpLow("Hello123 HELLO123 hello123!"))
'''

'''
# functions with default arguments
def foo(name, bonus=10):
    print(name, "made a bonus of", bonus, "points")
    
def main():
    foo("suma", 20)
    foo("tuan")
    foo("mary")
    foo("jim", 30)
    
main()
'''

'''
# local variables
def foo():
    x = 10
    print(x, "in foo")
    return x
    
def main():
    x = 5
    print(x, "in main")
    #foo()
    x = foo()
    print(x, "now in main again")  
    
main()
'''

'''
# global and local variables
x = 5
def foo():
    x = 0
    print(x, "in foo")
def main():
    print(x, "in main")
    foo()
    print(x, "now in main again")
main()
'''

# global variables
def foo():
    global x
    x = 0
    print(x, "in foo")
def main():
    #print(x, "in main")    
    foo()
    print(x, "now in main again")
main()
