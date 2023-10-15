 # Date: 9/29/2023
 # Author: Shantel Williams

# Problem: Create a function that takes a list of strings as input. Join each string in the list to create and return one complete string.
# Each word should have a space between them.

# Examples
# join_strings([“Hello”, “how”, “are”, “you?”]) -> “Hello how are you?”
# join_strings([“What’s”, “your”, “name?”]) -> “What’s your name?”
def join_strings(alist):
    return ' '.join(alist)
   

def main():
    tests = [
        join_strings(["Hello", "how", "are", "you?"]),
        join_strings(["What's", "your", "name?"])
    ]

    for t in tests:
        print(t)

main()