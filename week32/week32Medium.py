# Date: 8/14/2023
# Author: Shantel Williams

# Medium: Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.

# Examples:
# sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
# sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
# sum_common([1], [1], [2]) ➞ 0

def sum_common(lst1, lst2, lst3):
    """ Return the sum of integers which are common in all three lists. """
    sum = 0 # variable to hold sum 
    combined_list = lst1+lst2+lst3 # combined all three lists   Ex: [1, 2, 3, 5, 3, 2, 7, 3, 2]
    count_dict = {} # empty dictionary to store the number of repeats

    if not lst1 or not lst2 or not lst3: # case is a list is empty
        return "No common integers"

    for num in combined_list: # loop through all combined numbers,
        count_dict[num] = count_dict.get(num, 0) + 1  # am store the total count per number.    Ex. {1: 1, 2: 3, 3: 3, 5: 1, 7: 1}

    for num_key in count_dict: # since there is always 3 list, 
        if count_dict[num_key] % 3 == 0: # if the total count is a multiple of 3
            sum+=num_key * (count_dict[num_key]//3) # we add the number times the count divided by 3.   Ex. 2: 3, 3: 3 --> (2*1) + (3*1) = 5
    
    return sum

def main():
    test = sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) 
    test2 = sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) 
    test3 = sum_common([1], [1], [2]) 
    test4 = sum_common([1], [1,2], []) 
    print(test)
    print(test2)
    print(test3)
    print(test4)

main()