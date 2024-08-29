# Program to find lowest of 2 numbers

def getLowest(s1, s2):
    if (s1 < s2):
        return s1
    else:
        return s2

##################
# Declarations
##################
low=0
x=15
y=20

###############################
# I'm calling getLowest 4 times
###############################

low = getLowest(10,30)    # use commas to separate parameters
print("1: Lowest =", low)
low = getLowest(-5,-10)   # sending two parameters
print("2: Lowest =", low)

print("3: Lowest =", getLowest(x,y))
print("4: Lowest =", getLowest(100,y))
