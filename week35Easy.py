# Date: 7/25/2023
# Author: Shantel Williams

# Easy:
# 1. Write a Python function that takes a list of numbers and calculates the geometric mean.
# 3. Given input_list = [1, 2, 2, 45, 60, 3, 3, 3, 4, 5, 5]. Write a Python program to remove duplicates from the given list of values.
# Notes: You cannot use any python built-in function.

def mean(num_list):
    """ function that takes a list of numbers and calculates the geometric mean."""

    mean = 0  # set the mean variable to zero, it will be updated later in the function.]
    multiply = 1  # we will start by multiplying the first num by 1
    list_length = len(num_list)  # tells us how many number are in the list.

    for number in num_list:  # loop through list and multiply by the previous number
        multiply = multiply * number

    # I followed this formula -- geometric_mean = (multiply_values)**(1/n)
    # formula to find the geometric mean. Found at https://exploringfinance.com/geometric-mean-python/
    mean = multiply**(1/list_length)
    return mean  # return mean

def main():
    # mean function tests
    test = mean([2,18])
    print(test)

    test2 = mean([10, 51.2, 8])
    print(test2)

main()