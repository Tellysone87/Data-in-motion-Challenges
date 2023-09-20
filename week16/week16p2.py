 # Date: 9/20/2023
 # Author: Shantel Williams

# Problem 2: Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.

def even_num(alist):
    if not alist:
        return "No list provided."
    
    answer2 = [num for num in alist if num%2 == 0]

    return answer2

def main():

    giving_list2 = []
    test2 = even_num(giving_list2)
    print(test2)

    giving_list = [1,2,3,4,5,6]
    test = even_num(giving_list)
    print(test)

main()