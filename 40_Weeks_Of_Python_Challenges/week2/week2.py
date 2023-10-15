 # Date: 10/6/2023
 # Author: Shantel Williams



# Problem 1: Write a function that takes in an integer, minutes, and converts it into seconds
def convert_into_seconds(minutes):
    return minutes * 60

# Problem 2: Write a function that takes two numbers as arguments and returns their sum.
def sum(num1,num2):
    return num1 + num2


def main():
    test = [
        convert_into_seconds(2),
        sum(5,6)
    ]

    for t in test:
        print(t)


main()
