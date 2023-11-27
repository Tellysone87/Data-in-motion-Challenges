# 11/1/2023
# Shantel Williams

# Hard: Longest Consecutive Sequence
# Write a function longest_consecutive_sequence(nums) that takes a list of integers nums as input and returns the length of the longest consecutive sequence of numbers within the list.
# A consecutive sequence is a sequence of numbers that can be arranged in ascending order such that each number differs from the one before it by exactly 1.
# In the list [1, 2, 3, 5, 6], the longest consecutive sequence is [1, 2, 3] which has a length of 3.
# In the list [5, 5, 5, 5], the longest consecutive sequence is [5] which has a length of 1 (duplicates should be considered only once).
def longest_consecutive_sequence(nums): 
    sequence  = []
    start = min(nums)
    stop = len(nums) 
    i = 0

    #sort list sorted(nums)
    sort = sorted(nums)
    check = start

    #loop from the min number - min(nums) and check if the numbers match while incrementing ex. [1, 2, 3, 5, 6]
    while i < stop:
        if check == sort[i]: # 1 == 1, 2 == 2
            sequence.append(sort[i]) # [1, 2]
        else:
            break
        check +=1
        i +=1

    return sequence
    
def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 7, 8, 9, 1, 2, 3]
    list3 = [1, 3, 2, 4, 5, 7, 6, 9]
    list4 = [5, 5, 5, 5]
    list5 = [8,9,7,6,5]

    test = [ 
            longest_consecutive_sequence(list1),
            longest_consecutive_sequence(list2),
            longest_consecutive_sequence(list3),
            longest_consecutive_sequence(list4),
            longest_consecutive_sequence(list5)
            ]

    for t in test:
        print(t)

main()