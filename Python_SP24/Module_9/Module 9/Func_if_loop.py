
# Topics: Functions using selection (if) and repition (loop) structure.

def getHours():
    hours = int(input('Enter hours worked: '))
    return hours 

def findPay(hours):
    if hours <= 40:
        pay = hours * 30
    else:
        pay = (40 * 30) + ((hours - 40) * (hours * 1.5))
    return pay

def printPay(counter, pay):
    str1 = 'Employee #' + str(counter) + "'s pay is = $ " + str(format(pay, '.2f'))
    print(str1)

def main():
    repeat = 'y'
    counter = 1
    while repeat.lower() == 'y':
        hours = getHours()
        pay = findPay(hours)
        printPay(counter, pay)
        counter += 1
        repeat = input('Do you want to continue? ')

main()