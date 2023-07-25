# Date: 7/25/2023
# Author: Shantel Williams

# Expert: Create a function that returns the product of two integers. This process of multiplication can be achieved via repetitive addition, thus, the process can be done recursively.

# Examples:
# multiply(10, 2) ➞ 20
# multiply(-51, -4) ➞ 204
# multiply(3, 9) ➞ 27
# multiply(-21, 5) ➞ -105
# multiply(1024, 7) ➞ 7168
# multiply(273, -6) ➞ -1638

# Notes:
# You’re expected to solve this challenge using a recursive approach



def multiply(int1,int2, i = 0):
    """ Function that returns the product of two integers."""
    add = int1

    while i < int2:
        print(add)
        i+=1
        int1+=int1
        multiply(int1,int2,i)
       
    return add

def main():
    test = multiply(10, 2)

    print(test)

main()