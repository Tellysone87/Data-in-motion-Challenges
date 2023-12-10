# Shantel Williams
# 12/14/2023

# Easy: Convert Temperatures
# Data analysts working with environmental data may need to switch between temperature scales.

# Given a list of temperatures in Fahrenheit, create a function to convert them to Celsius.

# temperatures_in_fahrenheit = [32, 212, 100, 50, 80] => [0,100,37.7,10,26.6]

def convert_temp(list_of_fahrenheit_temp):
    # C equals °F minus 32, divided by 1.8
    return [(num - 32) / 1.8 for num in list_of_fahrenheit_temp]
    

def main():
    temperatures_in_fahrenheit = [32, 212, 100, 50, 80]

    print(convert_temp(temperatures_in_fahrenheit))

main()