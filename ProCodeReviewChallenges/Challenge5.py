# 1/16/2024
# Shantel Williams

# The code is meant to convert a list of strings to integers. However, it’s throwing an error when encountering a non-numeric string.

# https://d-i-motion.com/lessons/challenge-5/

def convert_to_int(input_list):
    return [int(i) for i in input_list if i.isnumeric()] ## added if statement to prevent the error occuring. 

print(convert_to_int(['1', '2', 'three']))
