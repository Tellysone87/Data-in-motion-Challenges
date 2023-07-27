# Date: 7/27/2023
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

def multiply(int1,int2):
    """ Function that returns the product of two integers."""

    if int1 == 0 or int2 == 0: # condition if any of the numbers are zero
        return 0
    
    if int2 > 0:
        if int2 == 1: # base condition for positive numbers 
            return int1
        return int1 + multiply(int1, int2 - 1)
        
    if int2 < 0:
        if int2 == -1:
            return int1
        return int1 + multiply(int1, int2 + 1)

def main():
    test = multiply(10, 2)
    test2 =  multiply(-51, -4)
    test3 = multiply(3, 9)
    test4 = multiply(-21, 5)
    test5 = multiply(1024, 7)
    test6 = multiply(273, -6)
    test7 = multiply(0,10)
    test8 = multiply(110,0)

    print(test)
    print(test2)
    print(test3)
    print(test4)
    print(test5)
    print(test6)
    print(test7)
    print(test8)

main()