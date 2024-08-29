# Program to display the total pennies collected in number of days entered by the user

# Declare variables for the number of pennies
# per day, the number of days, and the total
# number of pennies.

dayPennies = 1 
numDays = 0
total = 0.0

# Get number of days from the user.
numDays = int(input('Enter the number of days: '))

# Display table showing salary for each day.
print ('Day\tPennies')
print ('-------------------------')

for day in range(1, numDays + 1):
    print(day, '\t$', float(dayPennies / 100))
    total += dayPennies
    dayPennies *= 2

# Display total pay.
print('The total salary for', numDays,'days is: $',float(total/100))

# OUTPUT
'''
Enter the number of days: 10
Day	Pennies
-------------------------
1 	$ 0.01
2 	$ 0.02
3 	$ 0.04
4 	$ 0.08
5 	$ 0.16
6 	$ 0.32
7 	$ 0.64
8 	$ 1.28
9 	$ 2.56
10 	$ 5.12
The total salary for 10 days is: $ 10.23
'''
