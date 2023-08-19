# Date: 8/17/2023
# Author: Shantel Williams

# Medium: Python got drunk and the built-in functions str() and int() are acting odd

# str(4) ➞ 4
# str(“4”) ➞ 4
# int(“4”) ➞ “4”
# int(4) ➞ “4”

# You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers into strings and a function called str_to_int() that converts strings into integers.
# Examples:
# int_to_str(4) ➞ “4”
# str_to_int(“4”) ➞ 4
# int_to_str(29348) ➞ “29348”

# Notes:
# This is meant to illustrate the dangers of using already-existing function names.
# Extra points if you can de-drunk Python.

def int_to_str(int_num):
    """ Function called int_to_str() that converts integers into strings"""

    result = [] # list to hold the string numbers
    value_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'} # dictionary to store values
    mod = 10 # modulo operator will be updated eahch digit
    divide_by = 10 
    start  = 0 # keeps track of the number sum to stop loop
    round =1 # we need to track the fist round because the pattern is a little different

    # Here is the math pattern I figured out and implemented:
    # Digit = int_num % 10
    # Digit2 = int_num % 100 // 10
    # Digit3 = int_num % 1000 // 100
    # Digit....           ^       ^
    
    while start != int_num: # starts at zero
        if round == 1: # for round one, 
            digit = int_num % 10 # Digit = int_num % 10
            result.append(value_dict[digit]) # append Digit to list
            start +=digit # add the digit to start
        else:
            digit = int_num % mod // divide_by # after round 1, Digit2 = int_num % 100 // 10
            result.append(value_dict[digit]) # append the new digit
            start += digit * divide_by # add the digit times what it was divided by to keep incrementing our start until it reaches the provided value
            divide_by = divide_by * 10 # times the divide number by 10 to follow the pattern each round Ex. 10 > 100
        mod = mod *10 # same with mod Ex. 100 -> 100
        round +=1 # increment round to switch pattern
    
    return "".join(result[::-1]) # finally return reverse join on the list

def str_to_int(string_num):
    """ Function called str_to_int() that converts strings into integers."""
    result = 0 # set inital value to 0
    value_dict = {'0':0, '1':1, '2':2, '3':3, "4":4, '5':5, '6':6, '7':7, '8':8, '9':9} # dictionary to store values

    if len(string_num) == 1: # case if only on digit is provided
        return value_dict[string_num]
    
    for digit in string_num: # loop through each digit
            result = 10 * result + value_dict[digit] # we are performing this calculation each round

    return result # return result

def main():
    test = int_to_str(4) # provided test cases
    test2 = str_to_int("4")
    test3 = int_to_str(29348) 
    print(test)
    print(test2)
    print(test3)

main()

