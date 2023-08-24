# Date: 8/23/2023
# Author: Shantel Williams

# Hard: Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

# Examples:
# pluralize([“cow”, “pig”, “cow”, “cow”]) ➞ { “cows”, “pig” }
# pluralize([“table”, “table”, “table”]) ➞ { “tables” }
# pluralize([“chair”, “pencil”, “arm”]) ➞ { “chair”, “pencil”, “arm” }

# Notes:
# This is an oversimplification of the English language so no edge cases will appear.
# Only focus on whether or not to add an s to the ends of words.
# All tests will be valid.

def pluralize(list_of_words):
    """ Return a set of the words in the plural form if they appear more than once in the list."""

    Plural_set = set() # returns a set, so this is my initial set
    double_word = {} # dictionary to keep word count {Key: word , value: word occurrence count}

    # looping through list and storing the word count. 
    # This will help to check which words appear more that once
    for word in list_of_words: 
        if word not in double_word:
            double_word[word] = 1
        else:
            double_word[word] = double_word.get(word,0) + 1

    for count in double_word: # checking the dictionary to see which word appeared more than once 

        if double_word[count] > 1: # if the words value is greater than 1
            Plural_set.add(count +"s") # add the word to the set and add a "s" to the end per instructions

        elif double_word[count] == 1: # if the words value is only 1
            Plural_set.add(count) # just add the regular word

    return Plural_set # return the set. Sets are unordered so the words appearing in random order.

def main():
    test = pluralize(["cow", "pig", "cow", "cow"]) 
    test2 = pluralize(["table", "table", "table"])
    test3 = pluralize(["chair", "pencil", "arm"]) 
    print(test)
    print(test2)
    print(test3)

main()
