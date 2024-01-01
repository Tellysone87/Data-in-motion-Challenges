# 1/5/2024
# Shantel Williams

# https://d-i-motion.com/lessons/challenge-2/

# Problem
# The code is supposed to return the second largest number in a list. 
# However, it is currently not working as intended. Identify and fix the error.

def second_largest(numbers):
    largest = max(numbers)
    second_largest = max(numbers)
    for num in numbers:
        if num < largest and num > second_largest:
            second_largest = num
    return second_largest

numbers = [1, 2, 3, 4, 5]
print(second_largest(numbers)) # Expected: 4