# Date: 8/21/2023
# Author: Shantel Williams

# Very easy: Write a function that takes the base and height of a triangle and return its area.
# tri_area(3, 2) ➞ 3
# tri_area(7, 4) ➞ 14
# tri_area(10, 10) ➞ 50

# Notes:
# The area of a triangle is: (base * height) / 2
# Don’t forget to return the result.

def tri_area(base,height):
    """ Function that takes the base and height of a triangle and return its area."""
    results = base * height / 2 
    return int(results)
   

def main():
    test = tri_area(3, 2)
    test2 = tri_area(7, 4)
    test3 = tri_area(10, 10)
    print(test)
    print(test2)
    print(test3)

main()