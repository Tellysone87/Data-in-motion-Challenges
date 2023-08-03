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

    if not number_list: # empty list case
        return "empty list was provided"

    odd = 0 # holds odd sum
    even = 0 # holds even sum

    for number in number_list: # loop through list
        if number % 2 == 0: # if number is even
            even +=number # add it to the even sum
        else: # if not even
            odd+=number # add to the odd sum

    solution_list = [even,odd] # creating list for return
    return solution_list # returning solution list

def main():
    #tests
    test = sum_odd_and_even([1, 2, 3, 4, 5, 6]) 
    test2 = sum_odd_and_even([-1, -2, -3, -4, -5, -6]) 
    test3 = sum_odd_and_even([0, 0]) 
    test4 = sum_odd_and_even([]) 
    print(test)
    print(test2)
    print(test3)
    print(test4)

main()