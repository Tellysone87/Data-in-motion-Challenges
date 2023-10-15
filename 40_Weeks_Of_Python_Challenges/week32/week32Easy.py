# Date: 8/11/2023
# Author: Shantel Williams

# Easy: Create a function that replaces all the vowels in a string with a specified character.
# replace_vowels(“the aardvark”, “#”) ➞ “th# ##rdv#rk”
# replace_vowels(“minnie mouse”, “?”) ➞ “m?nn?? m??s?”
# replace_vowels(“shakespeare”, ““) ➞ “shkspr“

# Notes:
# All characters will be in lower case.

def replace_vowels(a_string,the_character):
    """ Function that replaces all the vowels in a string with a specified character."""

    index = 0 # starting our loop at the first letter
    stop = len(a_string) # variable for our stopping point
    string_list = [] # empty list to store any swaps
    vowel = ["a","e","o","i","u"] # letters to check for

    for index in range(stop): # loop through the provided string
        if a_string[index] in vowel: # check if that letter is a vowel
            string_list.append(the_character) # if so, add the character to the empty list
        else:
            string_list.append(a_string[index]) # if not, add the original letter instead. Example: ['t', 'h', '#', ' ', '#', '#', 'r', 'd', 'v', '#', 'r', 'k']

    new_list = "".join(string_list) # now we join the letters back together. # Example: th# ##rdv#rk

    return new_list 

def main():
    test1 = replace_vowels("the aardvark", "#") 
    test2 = replace_vowels("minnie mouse", "?") 
    test3 = replace_vowels("shakespeare", "") 
    print(test1)
    print(test2)
    print(test3)

main()