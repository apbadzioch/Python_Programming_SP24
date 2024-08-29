# Program to find lowest of 3 numbers

def getLowestOfThree(s1, s2, s3):
    if (s1 <= s2 and s1 <= s3):
        return s1
    elif (s2 <= s1 and s2 <= s3):
        return s2
    else:
        return s3

######################################
# I'm calling getLowestOfThree 3 times
######################################

print(getLowestOfThree(x,y,z))
print(getLowestOfThree(-9, x, 100))
low = getLowestOfThree(x,y,z)
print (low)
