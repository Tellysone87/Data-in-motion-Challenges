# Date: 8/7/2023
# Author: Shantel Williams

# Easy: Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.
# Examples:
# number_split(4) ➞ [2, 2]
# number_split(10) ➞ [5, 5]
# number_split(11) ➞ [5, 6]
# number_split(-9) ➞ [-5, -4]

# Notes:
# All numbers will be integers.
# You can expect negative numbers too.
# math.ceil rounds number up 
# math.floor rounds number down
import math

def number_split(input_number):

    if input_number == 0: # if zero is entered, return statement
        return "Zero cannot be split"

    if input_number % 2 == 0: # if number is even, return the halves
        halves = [int(input_number/2), int(input_number/2)]

    if input_number % 2 != 0: # if number is odd, return [half rounded down, half rounded up]
        halves = [math.floor(input_number/2), math.ceil(input_number/2)]

    return halves

def main():
    test = number_split(4)
    test2 = number_split(10)
    test3 = number_split(11)
    test4 = number_split(-9)
    print(test)
    print(test2)
    print(test3)
    print(test4)

main()