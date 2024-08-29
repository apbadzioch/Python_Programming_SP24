# Topics
'''
- format function on both numbers and strings
'''

# program description
'''
1.
Given the interest rate is 7.5%, have an user enter the
amount of purchase and display results as follows:

Example:
Enter the first amount of purchase: $100
Purchase Amt = $100.00
Interest Rate = 7.50%
Purchase Amt = $7.50
Purchase Amt = $107.50

2.
Extend the above example to receive another amount of purchase from the user and
create a report for two amounts as follows:

Example:
Enter the first amount of purchase: $100
Enter the second amount of purchase: $2222.22

   Purchase Amt  Interest Rate   Interest Amt      Total Amt
------------------------------------------------------------
        $100.00          7.50%          $7.50        $107.50
       $2222.22          7.50%        $166.67       $2388.89
'''

INTEREST_RATE = 0.075
COL1 = "Purchase Amt"
COL2 = "Interest Rate"
COL3 = "Interest Amt"
COL4 = "Total Amt"
LINE = '-' * 60
EQUAL_SYMBOL = " = "
DOLLAR_SYMBOL = '$'

purchaseAmt1 = float(input("Enter the first amount of purchase: $"))
interestAmt1 = purchaseAmt1 * INTEREST_RATE
totalAmt1 = purchaseAmt1 + interestAmt1

print((COL1 + EQUAL_SYMBOL + DOLLAR_SYMBOL + str(format(purchaseAmt1, '.2f'))))
print((COL2 + EQUAL_SYMBOL + str(format(INTEREST_RATE, '.2%'))))
print((COL1 + EQUAL_SYMBOL + DOLLAR_SYMBOL + str(format(interestAmt1, '.2f'))))
print((COL1 + EQUAL_SYMBOL + DOLLAR_SYMBOL + str(format(totalAmt1, '.2f'))))

purchaseAmt2 = float(input("\nEnter the second amount of purchase: $"))
interestAmt2 = purchaseAmt2 * INTEREST_RATE
totalAmt2 = purchaseAmt2 + interestAmt2

print()
print(format(COL1, ">15s"), end = '')
print(format(COL2, ">15s"), end = '')
print(format(COL3, ">15s"), end = '')
print(format(COL4, ">15s"))
print(LINE)

print(format(DOLLAR_SYMBOL + str(format(purchaseAmt1, ".2f")), ">15s"), end = '')
print(format(INTEREST_RATE, "15.2%"), end = '')
print(format(DOLLAR_SYMBOL + str(format(interestAmt1, ".2f")), ">15s"), end = '')
print(format(DOLLAR_SYMBOL + str(format(totalAmt1, ".2f")), ">15s"))

print(format(DOLLAR_SYMBOL + str(format(purchaseAmt2, ".2f")), ">15s"), end = '')
print(format(INTEREST_RATE, "15.2%"), end = '')
print(format(DOLLAR_SYMBOL + str(format(interestAmt2, ".2f")), ">15s"), end = '')
print(format(DOLLAR_SYMBOL + str(format(totalAmt2, ".2f")), ">15s"))















