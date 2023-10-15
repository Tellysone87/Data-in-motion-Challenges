# Date: 9/5/2023
# Author: Shantel Williams

# Write a function that transforms a list of characters into a list of dictionaries, 
# where: The keys are the characters themselves. The values are the ASCII codes of those characters.

# Examples:
# to_dict([“a”, “b”, “c”]) ➞ [{“a”: 97}, {“b”: 98}, {“c”: 99}]
# to_dict([“^”]) ➞ [{“^”: 94}]
# to_dict([]) ➞ {}

# Notes : Using Python ord() function. It returns the Unicode code from a given character.
def to_dict(provided_list):
    """ A function that transforms a list of characters into a list of dictionaries."""

    list_dict = [] # list to store dictionaries

    if not provided_list: # case if empty list is passed
        return {}
    
    for character in provided_list: # looping through provided list and
        convert = {character: ord(character)} # making a dictionary to hold the character(Key) and the ASCII value(Value)
        list_dict.append(convert) # adding the dictionary to my list

    return list_dict # return list of dictionaries

def main():
    tests = [
    to_dict(["a", "b", "c"]),
    to_dict(["^"]),
    to_dict([]) 
    ]

    for test in tests:
        print(test)
       

main()
