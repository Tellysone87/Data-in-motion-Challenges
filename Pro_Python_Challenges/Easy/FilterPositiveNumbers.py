# 10/20/2023
# Shantel Williams

# Using list comprehension, write a function named filter_positive_numbers that takes a list of integers as input 
# and returns a new list containing only the positive numbers from the input list.

# numbers = [-2, -1, 0, 1, 2]
def filter_positive_numbers(a_list):
    return [number for number in a_list if number > 0]

def main():
    numbers = [-2, -1, 0, 1, 2]
    test = filter_positive_numbers(numbers)

    print(test)

main()