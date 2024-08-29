#######################################
# Define functions at top
#######################################

def average(s1, s2, s3):       # define three parameters
    average = 0.0
    average = (s1+s2+s3)/3.0
    return average

#######################################
# I'm calling average 3 different times
#######################################

print(average(100,90,91))

## OR you can do it this way
answer = average(98,90,91)
print (answer)

## OR you can do it this way
test1=100
test2=90
test3=90
answer = average(test1,test2,test3)
print (answer)
