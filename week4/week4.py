 # Date: 10/11/2023
 # Author: Shantel Williams

# Bonus Points (Optional) Create a function that takes a number as an argument and returns “Fizz”, “Buzz” or “FizzBuzz”.
# If the number is a multiple of 3 the output should be “Fizz”. 
# If the number given is a multiple of 5, the output should be “Buzz”. 
# If the number given is a multiple of both 3 and 5, the output should be “FizzBuzz”. 
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below. 
# The output should always be a string even if it is not a multiple of 3 or 5.

def returnsCorrectString(giving_num):

    if giving_num == 0:
        return "Please provide a number over zero."
    
# If the number is a multiple of 3 the output should be “Fizz”. 
    if giving_num % 3 == 0 and giving_num % 5 != 0:
        return "Fizz"
   
# If the number given is a multiple of 5, the output should be “Buzz”. 
    if giving_num % 5 == 0 and giving_num % 3 != 0:
        return "Buzz"
   
# If the number given is a multiple of both 3 and 5, the output should be “FizzBuzz”. 
    if giving_num %3 == 0 and giving_num % 5 == 0:
        return  "FizzBuzz"

# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below. 
# The output should always be a string even if it is not a multiple of 3 or 5.
    else:
        return str(giving_num)
    
def main():
    tests = [
             returnsCorrectString(9),
             returnsCorrectString(25),
             returnsCorrectString(15),
             returnsCorrectString(2)
             ]
    
    for t in tests:
        print(t)
    


main()