########################################################
# 2. We go to the main function
#    and it calls myFirstFunction
# 4. Print "One more time:"
# 5. Then call myFirstFunction again
########################################################
def main():
    myFirstFunction()
    print("One more time:")
    myFirstFunction()

########################################################
# 3. Now we go to the myFirstFunction
#    and print the lines and we go back to main
# 6. And then we come back and print those lines again
########################################################

def myFirstFunction():
    print("Goodbye!")
    print("Come again!")

########################################################
# 1. This is first line in program
#    It is calling the main function
########################################################

main()
