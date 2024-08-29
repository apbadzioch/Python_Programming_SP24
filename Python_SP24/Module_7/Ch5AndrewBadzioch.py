# Name: Andrew Badzioch
# Program: Chapter 5 - Loops
# Description: This is a script that is a test grade calculator, with integer inputs ranging from 0-100. It will calculate the average test score
#              after dropping the lowest and assign a letter grade of A, B, C, D, or F. If the user inputs a number out of the given range, 
#              they will recieve an error message and be asked to input another number. Finally, the script will print out the lowest score that 
#              was dropped, the average after dropping rounded two decimal points and the letter grade that has been given.

# Constants
TITLE = "Hi, Welcome to the test grade calculator!\n"
LINE = '-' * len(TITLE)
NUM_TESTS = 3
A_GRADE = 90
B_GRADE = 80
C_GRADE = 70
D_GRADE = 60
ERROR = ('ERROR: Please make sure your number is between 0 and 100.')

# Print Program Title
print(TITLE+LINE)

# Input first test score and validate the range of 0-100
score1 = int(input("Please enter a score between 0 and 100: "))
while score1 < 0 or score1 > 100:
    print(ERROR)
    score1 = int(input("Please enter a score between 0 and 100: "))
score2 = int(input("Please enter another score: "))
while score2 < 0 or score2 > 100:
    print(ERROR)
    score2 = int(input("Please enter a score between 0 and 100: "))
score3 = int(input("And one last score: "))
while score3 < 0 or score3 > 100:
    print(ERROR)
    score3 = int(input("Please enter a score between 0 and 100: "))

# Find the lowest score of the 3
lowest = score1
if score2 < lowest:
    lowest = score2
if score3 < lowest:
    lowest = score3

# Find the average of the 3 scores and dividing by (NUM_TESTS - 1)
lowest = min(score1, score2, score3)
totalScore = score1 + score2 + score3 - lowest
avgScore = totalScore / (NUM_TESTS - 1)

# Using if/elif/else logic to find letterGrade of avgScore:
if avgScore >= A_GRADE:
    letterGrade = 'A'
elif avgScore >= B_GRADE:
    letterGrade = 'B'
elif avgScore >= C_GRADE:
    letterGrade = 'C'
elif avgScore >= D_GRADE:
    letterGrade = 'D'
else:
    letterGrade = 'F'

# Display the lowScore, avgScore, and letterGrade
print(LINE)
print("The lowest score dropped: ", lowest)
print("The average test score is: {:.2f}".format(avgScore))
print("The letter grade is: ", letterGrade)
print(LINE)