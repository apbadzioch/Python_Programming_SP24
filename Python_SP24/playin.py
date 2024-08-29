'''
def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result
    '''

def printGrade(score):                               # Print the grade for the score
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')
    
def main():                                         # Load the definition of the main function to the memory
    score = float(input('enter a score: '))
    print('the grade is: ', end="")                 # Statement to be displayed
    printGrade(score)                               # Invokes the printGrade function (no return value)

main()                                              # Call the main function





def printGrade(score):                               # Return the grade for the score
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'F'
    
def main():                                         # Load the definition of the main function to the memory
    score = float(input('emter a score: '))
    print('the grade is:', printGrade(score))       # Statement to be displayed
    #printGrade(score)                               # Invokes the printGrade function 

main()                                                                                          