 # Date: 9/21/2023
 # Author: Shantel Williams

# Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.

# Examples
# index_of_caps(“eDaBiT”) ➞ [1, 3, 5]
# index_of_caps(“eQuINoX”) ➞ [1, 3, 4, 6]
# index_of_caps(“determine”) ➞ []
# index_of_caps(“STRIKE”) ➞ [0, 1, 2, 3, 4, 5]
# index_of_caps(“sUn”) ➞ [1]
def index_of_caps(Some_string):
    # capital = []
    # i = 0

    # while i != len(Some_string):  ## While loop solution
    #     if Some_string[i].isupper():
    #         capital.append(i)
    #     i +=1
    
    return [Some_string.index(letter) for letter in Some_string if letter.isupper()]  # list comprehension solution

def main():
    test = [
    index_of_caps("eDaBiT"),
    index_of_caps("eQuINoX"),
    index_of_caps("determine"), 
    index_of_caps("STRIKE"), 
    index_of_caps("sUn") ]

    for t in test:
        print(t)

main()