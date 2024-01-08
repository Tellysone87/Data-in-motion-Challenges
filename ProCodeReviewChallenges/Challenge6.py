# 1/19/2024
# Shantel Williams

# The function is supposed to flatten a nested list. However, it’s throwing an error.

# https://d-i-motion.com/lessons/challenge-6/

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

print(flatten_list([1, 2, [3, 4, 5], 6]))
