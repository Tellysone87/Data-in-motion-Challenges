# Date: 8/22/2023
# Author: Shantel Williams

# Easy: Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

# Examples:
# factorial(3) ➞ 6
# factorial(5) ➞ 120
# factorial(13) ➞ 6227020800

# Notes:
# Assume all inputs are greater than or equal to 0.

def factorial(a_int):
    """ Function that takes an integer and returns the factorial of that integer."""
    fact = 1

    for i in range(1,a_int + 1):
        fact = fact * i 
        
    return fact


def main():
    test = factorial(3)
    test2 = factorial(5)
    test3 = factorial(13)
    print(test)
    print(test2)
    print(test3)

main()