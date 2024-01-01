# 1/9/2024
# Shantel Williams

# Problem:
# This code aims to swap the keys and values in a dictionary. But it doesn’t work as expected. Identify and fix the error.
# https://d-i-motion.com/lessons/challenge-3/

def swap_dict(dictionary):
    new_dict = {value: key for key, value in dictionary}
    return new_dict

my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(swap_dict(my_dict)) # Expected: {'a': 1, 'b': 2, 'c': 3}