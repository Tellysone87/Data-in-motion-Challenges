# Date: 8/29/2023
# Author: Shantel Williams

# Medium: Create a function that takes two number strings and returns their sum as a string.
# add(“111”, “111”) ➞ “222”
# add(“10”, “80”) ➞ “90”
# add(“”, “20”) ➞ “Invalid Operation”

def add(num1,num2):
    sum = 0

    if len(num1) == 0 or len(num2) ==0:
        return "Invalid Operation"
    
    num1_int = int(num1)
    num2_int = int(num2)

    sum = num1_int + num2_int
    return str(sum)

def main():
    test =add("111", "111") 
    test2 = add("10", "80") 
    test3 =add("", "20") 
    print(test)
    print(test2)
    print(test3)

main()