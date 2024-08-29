# nested loops

'''
Have the user enter 2 inputs: number of students in the class and
number of test scores to be entered for each student and then,
calculate and display the avg test score for each student.

For example:
Enter number of students: 2
Enter number of test scores: 3

Enter test score #1 for student #1: 66
Enter test score #2 for student #1: 77
Enter test score #3 for student #1: 100
Student #1 Avg = 81.00

Enter test score #1 for student #2: 66
Enter test score #2 for student #2: 77
Enter test score #3 for student #2: 100
Student #2 Avg = 81.00
'''

students = int(input("Enter number of students: "))
tests = int(input("Enter number of test scores: "))

for s in range(1, students+1):
    total = 0
    for t in range(1, tests+1):
        score = float(input("Enter test score #" + str(t) + \
                            "  for student #" +  str(s) + ": "))
        total += score
    avg = total/tests
    print("Student #" + str(s) + " Avg = " + str(format(avg, '.2f')))
