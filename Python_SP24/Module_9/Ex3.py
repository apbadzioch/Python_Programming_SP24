# Topics: Functions using selection (if) and repetition (loop) structures

# program description

'''
Use functions to do the following:
   - Receive the number of hours worked by the employee
   - find employee's pay based on the following rule:
       if hours worked is more than 40 hours then the employee is paid
       at a rate of 1.5 times the regular pay rate ($30/hour) for the extra hours worked
   - print the pay formatted to 2 decimals
   - Repeat the above until no more employee's pay to calculate

For example:
Enter hours worked: 40
Employee #1's pay = $1,200.00
Do you want to continue? y
Enter hours worked: 41
Employee #2's pay = $1,245.00
Do you want to continue? Y
Enter hours worked: 1
Employee #3's pay = $30.00
Do you want to continue? n
'''
REG_HOURS = 40
REG_PAY_RATE = 30.0
OT_PAY_RATE = 1.5 * REG_PAY_RATE

def main():
    repeat = 'y'
    counter = 1
    while repeat.lower() == 'y':
        hours = getHours()
        pay = findPay(hours)
        printPay(counter, pay)
        repeat = input("Do you want to continue? ")

def printPay(counter, pay):
    str1 = "Employee #" + str(counter) + "'s pay = $" + str(format(pay, ',.2f'))
    print(str1)
        
def findPay(hours):
    if hours <= REG_HOURS:
        pay = hours * REG_PAY_RATE
    else:
        pay = (REG_HOURS * REG_PAY_RATE) + (hours - REG_HOURS) * OT_PAY_RATE
    return pay

def getHours():
    hours = int(input("Enter hours worked: "))
    return hours

main()
    






    










