# Date : 5/24/2023
# Author: Shantel Williams
# Discription: challenge from week of 5/15/2023. Write a Python function that accepts a string as input and returns a dictionary containing the count of each character in the string. 
# For example, given the string "banana", the function should return {'b': 1, 'a': 3, 'n': 2}.


def letter_count(giving_string): # declare function
    letters = {} # set up empty library to hold letter counts
    for letter in giving_string: # loop through each letter
        if letter not in letters: # if letter is not present in the dictionary, add the letter with a count of 1
            letters[letter] = 1
        else:
            letters[letter] = letters.get(letter,0) + 1 # else just increment the letter value by one
    return letters # return the dictionary 


def main():
    i = "banana"
    print(letter_count(i)) # test function

main()