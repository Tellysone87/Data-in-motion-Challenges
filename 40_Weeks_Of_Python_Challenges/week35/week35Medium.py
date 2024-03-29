# Date: 7/25/2023
# Author: Shantel Williams

# Medium:
# 2. Given the following string, input_string, write a Python function that takes a string and removes all stop words (e.g. “the”, “a”, “an”) from it.
# input_string = “The quick brown fox jumps over the lazy dog”

# After research, I was able to find a stop word module that could help me with this function. Here is the documentation link - https://pypi.org/project/nltk/
# i then installed it for use with - python3 -m pip install nltk

# Natural language Toolkit designed to work with human language data - https://www.nltk.org/   ----   https://www.nltk.org/api/nltk.corpus.html
# provides a list of stop words. A stop word is a commonly used word that a search engine has been programmed to ignore. Straightforward - useless data/words. 
from nltk.corpus import stopwords

def string_manipulation(string_input):
    """ Function that takes a string and removes all stop words (e.g. “the”, “a”, “an”) from it."""

    index = 0 # variable to track our index 
    new_string = [] # I am using this list to store the words that are not stop words

    # nltk.download('stopwords') # you have to download the list once in the terminal
    stop_words = set(stopwords.words('english')) # grabbing the english stop words from the nltk module

    if not string_input: # condition if empty string is passed
        return "Empty string was provided"
    
    words = string_input.split(" ") # created a list from seperating each word in the string. This is for comparing. I am splitting on " ".
    
    while index < len(words): # looping through the word list
        if words[index].lower() not in stop_words: # if the lower case form of the index is not in the downloaded nltk list
            new_string.append(words[index]) # I am adding it to the new string list
        index += 1 # increment to avoid infinite while loop and move up the word list index

    return " ".join(new_string) # returned a string with all of the stop words removed

def main():
   input_string = "The quick brown fox jumps over the lazy dog"
   test = string_manipulation(input_string)
   print(test)

   input_string2 = ""
   test2 = string_manipulation(input_string2)
   print(test2)

main()