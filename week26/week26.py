# Date: 9/5/2023
# Author: Shantel Williams

# Write a function that transforms a list of characters into a list of dictionaries, 
# where: The keys are the characters themselves. The values are the ASCII codes of those characters.

# Examples:
# to_dict([“a”, “b”, “c”]) ➞ [{“a”: 97}, {“b”: 98}, {“c”: 99}]
# to_dict([“^”]) ➞ [{“^”: 94}]
# to_dict([]) ➞ {}

# Notes : Python ord() function returns the Unicode code from a given character.

def to_dict(provided_list):
    list_dict = []

    if not provided_list:
        return {}
    
    for character in provided_list:
        convert = {character: ord(character)}
        list_dict.append(convert)

    return list_dict


def main():
    tests = [
    to_dict(["a", "b", "c"]),
    to_dict(["^"]),
    to_dict([]) 
    ]

    for test in tests:
        print(test)
       

main()
