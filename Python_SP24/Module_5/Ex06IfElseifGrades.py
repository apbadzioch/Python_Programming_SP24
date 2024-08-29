# Grades Program

# Description: Have user enter a grade. Based on that grade, display the corresponding letter grade. 

testScore = float(input("Enter the test score: "))

if (testScore >= 90):
        print("--> A")
elif (testScore >= 80 and testScore < 90):
        print("--> B")
elif (testScore >= 70 and testScore < 80):
        print("--> C")
elif (testScore >= 60 and testScore < 70):
        print("--> D")
else:
        print("--> F")
        
# OUTPUT
# TEST RUN 1
'''
Enter the test score: 100
--> A
'''
# TEST RUN 2
'''
Enter the test score: 60
--> D
'''
# TEST RUN 3
'''
Enter the test score: 59
--> F
'''
