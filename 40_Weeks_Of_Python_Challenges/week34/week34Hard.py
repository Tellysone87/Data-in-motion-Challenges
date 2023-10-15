# Date: 8/3/2023
# Author: Shantel Williams

# Hard: Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
# Examples:
# majority_vote([“A”, “A”, “B”]) ➞ “A”
# majority_vote([“A”, “A”, “A”, “B”, “C”, “A”]) ➞ “A”
# majority_vote([“A”, “B”, “B”, “A”, “C”, “C”]) ➞ None

# Notes:
# The frequency of the majority element must be strictly greater than 1/2.
# If there is no majority element, return None.
# If the list is empty, return None.

def majority(provided_list):
    majority_vote = "None" # If there is no majority element, return None.
    count_library = {} # dictionary to hold count. the letter as the key and the count as the value. 

    if not provided_list: #If the list is empty, return None.
        return "None"
   
    for letter in provided_list: # loop through provided list and add count for each occurance to library value
        if letter  not in count_library: # if letter is not alreay a key, add it with a value of one
            count_library[letter] = 1
        else: 
            count_library[letter] = count_library.get(letter,0) + 1 # else increment the letter value by one

     # occurs > N/2 times in a list (where N is the length of the list).
    for record in count_library: # go through record and check each key value against the majority formula
        if count_library[record] > len(provided_list)/2: # if condiion exists, this is the majority
            majority_vote = record

    return majority_vote

def main():
    test = majority(["A", "A", "B"])
    test2 = majority(["A", "A", "A", "B", "C", "A"])
    test3 = majority(["A", "B", "B", "A", "C", "C"])

    print(test)
    print(test2)
    print(test3)

main()