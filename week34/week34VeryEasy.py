# Date: 7/31/2023
# Author: Shantel Williams

# Very easy: Write a function that takes the base and height of a triangle and return its area.

# Examples:
# tri_area(3, 2) ➞ 3
# tri_area(7, 4) ➞ 14
# tri_area(10, 10) ➞ 50

# Notes:
# The area of a triangle is: (base * height) / 2
# Don’t forget to return the result.

def area(the_base, the_height):
    """ Function that takes the base and height of a triangle and return its area. """

    area = (the_base * the_height) / 2 # formula for area

    return area # return area

def main():
    test = area(20,50) # test case

    print(test)

main()