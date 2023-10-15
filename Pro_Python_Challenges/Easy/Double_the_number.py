# Date: 10/13/2023
# Author: Shantel Williams

# Problem 1: Using list comprehension, write a function named double_numbers that takes a list of integers as input 
# and returns a new list where each element is twice the corresponding element from the input list.

# numbers = [1, 2, 3, 4, 5]
def double_numbers(some_list):

    return [num * 2 for num in some_list]

def main():
    numbers = [1, 2, 3, 4, 5]
    test = double_numbers(numbers)
    print(test)


main()