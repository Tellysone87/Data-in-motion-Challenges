# Date: 10/11/2023
 # Author: Shantel Williams

# Problem 1: Create a function that takes a string and returns the number (count) of vowels contained within it.

def vowelCount(word):
    count = 0
    vowels= ["a","e","i","o","u"]

    for letter in word:
        if letter.lower() in vowels:
            count +=1

    return count


def main():
    test = [ 
        vowelCount("meal"),
        vowelCount("hOuse"),
        vowelCount("shop"),
        vowelCount("jump")]
    
    for t in test:
        print(t)
main()