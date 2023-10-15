# Date: 8/8/2023
# Author: Shantel Williams

# Medium: Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.

# Examples:
# list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
# list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

# Notes:
# Notice that num is also included in the returned list.

def list_of_multiples(num,length):
    """ Function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length."""
    new_list = [] # empty list to add multiples
    stop = length # where to stop list
    i = 1 # count holder

    if num == 0: # case if 0 is entered for number
        return "multiples of zero are zero"

    while i <= stop: # loop for multiples
        mulitple = i * num
        new_list.append(mulitple) # append each multiple to list
        i +=1 # increment counter

    return new_list # return list 

def main():
    test1 = list_of_multiples(7, 5)
    test2 = list_of_multiples(12, 10) 
    test3 = list_of_multiples(17, 6) 
    print(test1)
    print(test2)
    print(test3)


main()