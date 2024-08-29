# Topics
'''
- Common python functions
    -- Built-in functions: abs, max, min, pow, round, format
    -- Math functions (import math): ceil, floor, sqrt, exp, hypot, etc.
'''

# program description
'''
Have the user enter the two sides of a right angled triangle.
Find and display the hypotenuse (hypo = sqaure root(s1 squared + s2 squared))
'''
import math

'''
s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))

print()
print("Finding Hypotenuse using...")
hypo = (s1 * s1 + s2 * s2) ** (1/2)
print("no functions method #1:", hypo)

hypo = (s1 ** 2 + s2 ** 2) ** (1/2)
print("no functions method #2:", hypo)

hypo = math.hypot(s1, s2)
print("hypot function:", hypo)

hypo = math.sqrt(s1 * s1 + s2 * s2)
# hypo = math.sqrt(s1 ** 2 + s2 ** 2)
print("sqrt function:", hypo)

s1 = -10
print("using abs function:", abs(s1))

hypo = math.sqrt(pow(s1, 2) + pow(s2, 2))
print("sqrt and pow functions:", hypo)

print()
print("ceil function", math.ceil(hypo))
print("floor function", math.floor(hypo))
print("int function", int(hypo))
print("round function", round(hypo))

print()
print("ceiling function")
print("12.4:", math.ceil(12.4))     #13
print("12.5:", math.ceil(12.5))     #13
print("12.6:", math.ceil(12.6))     #13
print("11.5:", math.ceil(11.5))     #12

print()
print("floor function")
print("12.4:", math.floor(12.4))     #12
print("12.5:", math.floor(12.5))     #12
print("12.6:", math.floor(12.6))     #12
print("11.5:", math.floor(11.5))     #11

print()
print("int function")
print("12.4:", int(12.4))     #12
print("12.5:", int(12.5))     #12
print("12.6:", int(12.6))     #12
print("11.5:", int(11.5))     #11
'''

print()
print("round function")
print("12.4:", round(12.4))     #12
print("12.5:", round(12.5))     #12
print("12.6:", round(12.6))     #13
print("11.5:", round(11.5))     #12
print("14.51:", round(14.51))   #













