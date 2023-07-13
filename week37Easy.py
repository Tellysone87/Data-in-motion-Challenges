# Date: 7/14/2023
# Author: Shantel Williams

# Easy: Write a Python function that accepts a string as input 
# and returns a dictionary containing the count of each character in the string. 
# For example, given the string “banana”, the function should return {‘b’: 1, ‘a’: 3, ‘n’: 2}.

def letter_count(Provided_String):
    """ function that accepts a string as input and returns a dictionary containing the count of each character in the string. """
    letter_Dict = {} # empty dictionary to hold letter count

    if not Provided_String: # if passed emptty string
        return "No string was provided"

    for letter in Provided_String: # loop through string
        letter_Dict[letter] = letter_Dict.get(letter, 0) + 1 # add the key and 1 to the value

    return letter_Dict # return dictionary
    
def main():
    test = letter_count("banana") # test function
    print(test)

    print(letter_count("")) # returjs empty dictionary

main()