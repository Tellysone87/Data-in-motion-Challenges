# 1/2/2024
# Shantel Williams

# https://d-i-motion.com/lessons/challenge-1/

# Dictionary Manipulation

# Problem:The task of the following code is to count the frequency of words in a list, storing the counts in a dictionary, 
# and print the most common word. Identify and fix the error.

words = ['apple', 'banana', 'apple', 'cherry', 'cherry', 'cherry']

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1   ## word_counts[word] + 1 - this was not the correct way to update a key value. 

most_common_word = max(word_counts, key = word_counts.get)
print(most_common_word)