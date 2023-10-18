# 10/23/2023
# Shantel Williams

# Using list comprehension, write a function named extract_vowels that takes a list of strings as input 
# and returns a new list containing only the vowels from all the strings in the input list.

# strings = [‘apple’, ‘banana’, ‘orange’]
def extract_vowels(list_of_strings):
   combined_list = "".join(list_of_strings)
   return [letter for letter in combined_list if letter.lower() in ["a","e","i","o","u"]]

def main():
    strings = ['apple', 'banana', 'orange']
    test = extract_vowels(strings)
    print(test)

main()