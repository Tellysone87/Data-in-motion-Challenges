# Date: 8/29/2023
# Author: Shantel Williams

# Hard: Create a function that counts the number of digits in a number. 
# Conversion of the number to a string is not allowed.

# digits_count(4666) ➞ 4
# digits_count(544) ➞ 3
# digits_count(121317) ➞ 6
# digits_count(0) ➞ 1
# digits_count(12345) ➞ 5
# digits_count(1289396387328) ➞ 13
def digits_count(num):
    count = 0
    i = num

    if num == 0: # test case if number = 0
        return 1

    if num > 1: # if number in argumentis greater than 1
        while i > 1:
            i = i/10
            count +=1

    if num < 1: # if number in argument is less than 1
        while i < -1:
            i = i/10
            count +=1
    return count

def main():
    testcases = [
     digits_count(4666) , # positive
     digits_count(544) ,
     digits_count(121317) ,
     digits_count(0) ,
     digits_count(12345),
     digits_count(1289396387328),

     digits_count(-12893), # negtive
     digits_count(-456),

     digits_count(6)] # single digit
   
    for test_case in testcases:
        print(test_case)
main()