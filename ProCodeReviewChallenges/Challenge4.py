# 1/12/2024
# Shantel Williams

# The code is supposed to handle a division by zero exception, but it’s still throwing an error.
# https://d-i-motion.com/lessons/challenge-4/

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = 'Cannot divide by zero' # original line - print('Cannot divide by zero')
    finally:
        return result

print(divide_numbers(4, 0))