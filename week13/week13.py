 # Date: 9/25/2023
 # Author: Shantel Williams

# Problem: Create a function that takes a number as its only argument and returns True if it’s less than or equal to zero, otherwise return False.

# Examples:
# less_than_or_equal_to_zero(5) ➞ False
# less_than_or_equal_to_zero(0) ➞ True
# less_than_or_equal_to_zero(-2) ➞ True
def less_than_or_equal_to_zero(_number):

    return _number <= 0



def main():
    tests = [ 
    less_than_or_equal_to_zero(5), 
    less_than_or_equal_to_zero(0), 
    less_than_or_equal_to_zero(-2) ]

    for test in tests:
        print(test)
    


main()