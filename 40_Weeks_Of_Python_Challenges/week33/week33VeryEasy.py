# Date: 8/4/2023
# Author: Shantel Williams

# Very easy: Create a function that takes a number as an argument, increments the number by +1 and returns the result.
# Examples:
# addition(0) ➞ 1
# addition(9) ➞ 10
# addition(-3) ➞ -2

# Notes
# Don’t forget to return the result.
def addition(giving_number):
    giving_number += 1 # add 2 to the number provided
    return giving_number

def main():
    all_test = [addition(0),addition(9),addition(-3)]
    print(all_test)

main()