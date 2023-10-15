 # Date: 9/19/2023
 # Author: Shantel Williams

# Problem 1: Given a list [“Elie”, “Tim”, “Matt”], create a variable called answer, 
# which is a new list containing the first letter of each name in the list.

def first_letter(provided_list):

    answer = [name[0] for name in provided_list] # used list comprehension
    return answer


def main():
    test = ["Elie", "Tim", "Matt"]
    print(first_letter(test))

main()