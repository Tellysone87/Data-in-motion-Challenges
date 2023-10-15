# Date: 8/1/2023
# Author: Shantel Williams

# Easy: Create a function that takes an integer and returns the factorial of that integer. 
# That is, the integer multiplied by all positive lower integers.
# Examples:
# factorial(3) ➞ 6 3*2 , #*1
# factorial(5) ➞ 120
# factorial(13) ➞ 6227020800

# Notes:
# Assume all inputs are greater than or equal to 0.
def factorial(a_interger):
    """ Function that takes an integer and returns the factorial of that integer."""
    if a_interger == 1: # base case
        return a_interger
    if a_interger < 0: # per instructions, giving number should be positive. 
        return("please use positive numbers")
    
    return a_interger*factorial(a_interger-1) # factorial solution

def main():
    # test cases provided for challenge
    test = factorial(3)
    test2 = factorial(5)
    test3 = factorial(13)
    print(test)
    print(test2)
    print(test3)

main()