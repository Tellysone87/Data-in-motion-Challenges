# Date: 8/17/2023
# Author: Shantel Williams

# Easy: Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
# Examples:
# find_even_nums(8) ➞ [2, 4, 6, 8]
# find_even_nums(4) ➞ [2, 4]
# find_even_nums(2) ➞ [2]
# Try to use list comprehensions in your solution. Here’s an example:

# vals = [expression
# for value in collection
# if condition]
# This is equivalent to:

# vals = []
# for value in collection:
# if condition:
# vals.append(expression)

# Notes:
# Try to use list comprehensions instead of logic.
# If there are no even numbers, return an empty list.
def find_even_nums(num):
    """ Function that finds all even numbers from 1 to the given number. """

    even_nums = [i for i in range(1, num + 2) if i % 2 == 0 ]

    return even_nums

def main():
    test = find_even_nums(8)
    test2 =find_even_nums(4)
    test3 = find_even_nums(2)
    print(test)
    print(test2)
    print(test3)

main()