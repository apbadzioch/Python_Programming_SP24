#######################################
# Define functions at top
#######################################

def main():
    ## OR you can input it from user
    test1 = int(input("Enter test1: "))
    test2 = int(input("Enter test1: "))
    test3 = int(input("Enter test1: "))
    print(average(test1,test2,test3))

def average(s1, s2, s3):
    average = 0.0
    average = (s1+s2+s3)/3.0
    return average

##############################################
# Call main and then have main call everything
##############################################

main()
