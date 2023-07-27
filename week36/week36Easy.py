# Date: 7/20/2023
# Author: Shantel Williams

# Easy: Create a function that takes a string and returns the number (count) of vowels contained within it.

# Examples:
# count_vowels(“Celebration”) ➞ 5
# count_vowels(“Palm”) ➞ 1
# count_vowels(“Prediction”) ➞ 4

def num_of_vowels(a_string):
    """ Function that takes a string and returns the number (count) of vowels contained within it. """

    count = 0 # set count variable to keep track of vowels
    vowels = ["a","e","i","o","u"] # added vowels to a list to check each letter against

    for letter in a_string.lower(): # checking each letter in the string against the vowel list after making sure its lower case.
        if letter in vowels:
            count +=1 # if letter is in vowel, add 1 to our count

    return count # return the count

def main():
    test1 = num_of_vowels("Palm")
    print(test1)

    test2 = num_of_vowels("Prediction")
    print(test2)

    test3 = num_of_vowels("Application")
    print(test3)

main()