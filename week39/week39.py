# Date : 5/30/2023
# Author: Shantel Williams
# Discription: Write a Python function that takes the following dictionary as input 
# and returns a new dictionary where the keys and values are swapped. 
# In other words, the function should create a new dictionary where the original values become the keys,
# and the original keys become the values.

# original_dict = {“apple”: 1, “banana”: 2, “cherry”: 3}


def swap_key_and_values(current_dictionary):

    new_dict = {} # creating new empty Dictionary
    for item in current_dictionary: # iterate through the original list and add the values to the empty dictionary
        new_dict[current_dictionary[item]]  = item # we are grabbing the items value as the key and setting the item as the value

    return new_dict # return new list
       

def main():
    original_dict = {"apple": 1, "banana": 2, "cherry": 3}
    print(swap_key_and_values(original_dict))


main()