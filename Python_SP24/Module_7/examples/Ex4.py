# TOPIC: for and while loop
'''
Have the user enter the temperature in fahrenheit for the entire week and
display the temp in fah and it's corresponding celsius 
value (given formula: c = (f-32)*5/9) and also display the average temp
for the week in both fah and cel.

For example:
Enter temp in fahrenheit for Day #1: 100
100F = 37.78C

Enter temp in fahrenheit for Day #2: 99
99F = 37.22C

Enter temp in fahrenheit for Day #3: 88
88F = 31.11C

Enter temp in fahrenheit for Day #4: 77
77F = 25.00C

Enter temp in fahrenheit for Day #5: 66
66F = 18.89C

Enter temp in fahrenheit for Day #6: 55
55F = 12.78C

Enter temp in fahrenheit for Day #7: 32
32F = 0.00C

--------------------------------------------------
Average Temp for this week was: 73.86F = 23.25C
--------------------------------------------------
'''
DAYS = 7
LINE = '-' * 50

sumFah = sumCel = 0.0
for i in range(1, DAYS+1):
    tempFah = int(input("Enter temp in fahrenheit for Day #" + str(i) + ": "))
    tempCel = (tempFah - 32) * (5 / 9)
    print(str(tempFah) + "F = " + str(format(tempCel, '.2f')) + "C\n")
    # print()
    sumFah += tempFah
    sumCel += tempCel
avgFah = sumFah/DAYS
avgCel = sumCel/DAYS

print(LINE)
print("Average Temp for this week was:", end = ' ')
print(str(format(avgFah, '.2f')) + "F = " + str(format(avgCel, '.2f')) + "C")
print(LINE)
print("\n\n")

sumFah = sumCel = 0.0
i = 1
while i < DAYS+1:
    tempFah = int(input("Enter temp in fahrenheit for Day #" + str(i) + ": "))
    tempCel = (tempFah - 32) * (5 / 9)
    print(str(tempFah) + "F = " + str(format(tempCel, '.2f')) + "C\n")
    # print()
    sumFah += tempFah
    sumCel += tempCel
    i += 1
avgFah = sumFah/DAYS
avgCel = sumCel/DAYS

print(LINE)
print("Average Temp for this week was:", end = ' ')
print(str(format(avgFah, '.2f')) + "F = " + str(format(avgCel, '.2f')) + "C")
print(LINE)





    
