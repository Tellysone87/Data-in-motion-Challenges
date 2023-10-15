# Date: 7/24/2023
# Author: Shantel Williams

# Hard: Create a function that takes in two words as input and returns a list of three elements, in the following order:
# 1. Shared letters between two words.
# 2. Letters unique to the first word
# 3. Letters unique to the second word. Each element should have unique letters, and have each letter be alphabetically
# sorted.

# Examples:
# letters(“sharp”, “soap”) ➞ [“aps”, “hr”, “o”]
# letters(“board”, “bored”) ➞ [“bdor”, “a”, “e”]
# letters(“happiness”, “envelope”) ➞ [“enp”, “ahis”, “lov”]
# letters(“kerfuffle”, “fluffy”) ➞ [“flu”, “ekr”, “y”]
# letters(“match”, “ham”) ➞ [“ahm”, “ct”, “”]

def letters(word1,word2):
    """ A function that takes in two words as input and returns a list of three elements"""

    #setting an empty string to store each value per index
    common_letters = "" # Shared letters between two words. [0]
    unique_letters_first_word = "" # Letters unique to the first word [1]
    unique_letter_second_word = ""  # Letters unique to the second word [2]
    i = 0 # varaible to keep track of index

    set1 = set(word1) # creating sets for the word strings to remove duplicates
    set2 = set(word2)

    for letter in set1: # looping through the first set
    # Shared letters between two words.
        if letter in set2:
            common_letters = common_letters + letter

    # Letters unique to the first word.
        if letter not in set2:
            unique_letters_first_word  = unique_letters_first_word + letter

    # Letters unique to the second word.
    for letter in set2:
        if letter not in set1:
            unique_letter_second_word = unique_letter_second_word + letter

    answer_list = [sorted(common_letters), sorted(unique_letters_first_word), sorted(unique_letter_second_word)] # sorting each condition list Ex. [['a', 'p', 's'], ['h', 'r'], ['o']]

    for sort_list in answer_list:
        answer_list[i] = "".join(sort_list) # joining each letter per list for the desired result Ex. [['a', 'p', 's'], ['h', 'r'], ['o']] ==> ['aps', 'hr', 'o']
        i+=1
       
    return answer_list
    
def main():
    test = letters("sharp", "soap")
    test2 = letters("board", "bored")
    test3 = letters("match", "ham")
    print(test)
    print(test2)
    print(test3)
main()