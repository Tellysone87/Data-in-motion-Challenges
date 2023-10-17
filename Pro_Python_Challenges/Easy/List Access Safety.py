# 10/17/2023
# Shantel Williams

# Create a Python function that takes in a dictionary and a key, and then returns the value corresponding to that key from the dictionary.
# If the key is not present in the dictionary, the function should return a custom error message.

# Parameters
# Your function should accept the following parameters:
# input_dict: A dictionary from which you need to retrieve the value.
# lookup_key: The key for which you are looking up the value.

# Example Usage:
# If input_dict is {'apple': 5, 'banana': 7} and lookup_key is 'apple', the function should return 5.
# If input_dict is {'apple': 5, 'banana': 7} and lookup_key is 'orange', the function should return a custom error message like “Key not found”.


def find_value(input_dict, lookup_key):
    if lookup_key not in input_dict:
        return "key not found."
    
    return input_dict[lookup_key]



def main():
    input_dictionary = {'apple': 5, 'banana': 7}

    test =  [find_value(input_dictionary, 'apple'),
             find_value(input_dictionary, "grape")
             ]
    
    for t in test:
        print(t)

main()