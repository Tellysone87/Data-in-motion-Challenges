# Date: 9/12/2023
# Author: Shantel Williams


# Write a function called single_letter_count. This function takes in two parameters (two strings). 
# The first parameter should be a word and the second should be a letter. 
# The function returns the number of times that letter appears in the word. 
# The function should be case insensitive (does not matter if the input is lowercase or uppercase). 
# If the letter is not found in the word, the function should return 0.

def single_letter_count(string1,string2):
    """ function returns the number of times that letter appears in the word. """
    count = 0 ## initial count

    for letter in string1.lower(): ## loop through the first string lower cased
        if string2.lower() == letter: ## check for the provided letter
            count +=1 ## If letter mathces the current word letter in loop, add one to count

    return count


def main():
    test = [ 
        single_letter_count("banana","n"),
        single_letter_count("test","t"),
        single_letter_count("STATUS","s"),
        single_letter_count("choice","z")]
    
    for t in test:
        print(t)


main()