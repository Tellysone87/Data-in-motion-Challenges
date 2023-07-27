# Date: 7/25/2023
# Author: Shantel Williams

# Easy:
# 1. Write a Python function that takes a list of numbers and calculates the geometric mean.
# 3. Given input_list = [1, 2, 2, 45, 60, 3, 3, 3, 4, 5, 5]. Write a Python program to remove duplicates from the given list of values.
# Notes: You cannot use any python built-in function.

def mean(num_list):
    """ function that takes a list of numbers and calculates the geometric mean."""

    mean = 0  # set the mean variable to zero, it will be updated later in the function.
    multiply = 1  # we will start by multiplying the first num by 1
    list_length = len(num_list)  # tells us how many number are in the list.

    # if list is empty
    if list_length == 0:
        return "No numbers provided"
    
    # condition for negative numbers
    for num in num_list:
        if num <= 0:
            return "please enter postive numbers"

    # # steps is negative numbers are present
    # for number in num_list: # for number in list
    #     if number < 0: # if there is a negative number
    #         while i <= list_length - 1: # starting at the first index
    #             num_list[i] = num_list[i]/100 # we multiply the number by 100 to get decimal
    #             print(num_list[i])
    #             if num_list[i] > 0: # next we add 1 if the number is positive or subtract 1 if the number is negative
    #                 num_list[i] = 1 + num_list[i]
    #                 print(num_list[i])
    #                 multiply = multiply * num_list[i]
                    
    #             elif num_list[i]  < 0:
    #                num_list[i]  = 1 + num_list[i]
    #                print(num_list[i])
    #                multiply = multiply *  num_list[i]
    #             i+=1
    #         print(multiply)
    #         root_of = 1/list_length
    #         mean = pow(multiply, root_of) 
    #         print(mean -1)
    #         print(mean*100)
    #         return mean * 100
                
    # Condition for positive numbers          
    for number in num_list:  # loop through list and multiply by the previous number
        multiply = multiply * number

    # I followed this formula -- geometric_mean = (multiply_values)**(1/n)
    # formula to find the geometric mean. Found at https://exploringfinance.com/geometric-mean-python/
    mean = multiply**(1/list_length)
    return mean  # return mean

def main():
    # mean function tests
    test = mean([2,-18])
    print(test)

    test2 = mean([10, 51.2, 8])
    print(test2)

    test3 = mean([])
    print(test3)

main()