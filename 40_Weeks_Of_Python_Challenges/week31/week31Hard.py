# Date: 8/21/2023
# Author: Shantel Williams

# Hard: Create a function that creates a box based on dimension n.
# Examples:
# make_box(5) ➞ [
# “#####”,
# “# #”,
# “# #”,
# “# #”,
# “#####”
# ]

# make_box(3) ➞ [
# “###”,
# “# #”,
# “###”
# ]

# make_box(2) ➞ [
# “##”,
# “##”
# ]

# make_box(1) ➞ [
# “#”
# ]
def make_box(num):
    """ Function that creates a box based on dimension n."""
    box_list = []
    i = 1
    
    while i <= num: # loop until the rows match the num
        if i == 1 or i == num: # if row is equal to one or num, append "#" * num
            box_list.append("#" * num)
        else: # else, append "# #"
            box_list.append("# #")
        i+=1

    return box_list

def main():
    test = make_box(5)
    test2 = make_box(3)
    test3 = make_box(2)
    test4 = make_box(1)
    print(test)
    print(test2)
    print(test3)
    print(test4)

main()