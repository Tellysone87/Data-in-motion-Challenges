# 10/19/2023
# Shantel Williams

# Write a Python function that accepts a dictionary and a key, 
# and attempts to return the value associated with the key in the dictionary.
# The function should handle the KeyError exception and return None if such an error occurs.
def safe_dict_access(dict, key):
    try:
        return dict[key]
    
    except KeyError:
        return None


def main():
    test= [safe_dict_access({'a': 1, 'b': 2, 'c': 3}, 'd'),
           safe_dict_access({'a': 1, 'b': 2, 'c': 3}, 'b')
           ]
    
    for t in test:
        print(t)

main()