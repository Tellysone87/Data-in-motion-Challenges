# Date: 8/2/2023
# Author: Shantel Williams

# Medium: Write a function that takes a list of numbers and returns a list with two elements:

# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

# Example:
# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
# sum_odd_and_even([0, 0]) ➞ [0, 0])

def sum_odd_and_even(number_list):
    """ Function that takes a list of numbers and returns a list with two elements:"""

    odd = 0 # holds odd sum
    even = 0 # holds even sum

    for number in number_list:
        if number % 2 == 0:
            even +=number
        else:
            odd+=number

    solution_list = [even,odd] # creating empty list for return
    return solution_list

def main():
    #tests
    test = sum_odd_and_even([1, 2, 3, 4, 5, 6]) 
    test2 = sum_odd_and_even([-1, -2, -3, -4, -5, -6]) 
    test3 = sum_odd_and_even([0, 0]) 

    print(test)
    print(test2)
    print(test3)

main()