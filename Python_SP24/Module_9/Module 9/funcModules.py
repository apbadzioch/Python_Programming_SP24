
# Topics: How functions can be used as modules.

# All the def functions will be put into different files and imported to run main()

import mod1
import mod2

TITLE = "Welcome to the sum of 2 numbers program!"
LINE = "-" * len(TITLE)

def main():
    mod1.printTitle()
    num1, num2 = mod1.getNum()
    total = mod2.findTotal(num1, num2)
    mod2.printTotal(num1, num2, total)
    print(LINE)

main()