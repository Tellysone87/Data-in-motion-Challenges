# Date: 7/20/2023
# Author: Shantel Williams

# Easy: Create a function that takes a string and returns the number (count) of vowels contained within it.

# Examples:
# count_vowels(“Celebration”) ➞ 5
# count_vowels(“Palm”) ➞ 1
# count_vowels(“Prediction”) ➞ 4

def num_of_vowels(a_string):
    count = 0
    vowels = ["a","e","i","o","u"]

    for letter in a_string:
        if letter in vowels:
            count +=1

    return count

def main():
    test1 = num_of_vowels("Palm")
    print(test1)

    test2 = num_of_vowels("Prediction")
    print(test2)

main()