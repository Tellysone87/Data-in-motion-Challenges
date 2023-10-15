# Date: 8/9/2023
# Author: Shantel Williams

# Very easy: Create a function that takes voltage and current and returns the calculated power.
# Power = Voltage x Current

# Examples:
# circuit_power(230, 10) ➞ 2300
# circuit_power(110, 3) ➞ 330
# circuit_power(480, 20) ➞ 9600

def circuit_power(voltage,current):
    """ Function that takes voltage and current and returns the calculated power. """
    calculated_power = 0

    # Power = Voltage x Current
    calculated_power = voltage * current

    return calculated_power

def main():
    test1 = circuit_power(230, 10)
    test2 = circuit_power(110, 3)
    test3 = circuit_power(480, 20)
    print(test1)
    print(test2)
    print(test3)

main()


