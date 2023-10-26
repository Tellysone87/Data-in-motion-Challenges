# 10/30/2023
# Shantel Williams

# Write a function reverse_tuple(t) that takes a tuple t as input and returns a new tuple with the elements in reverse order.

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = ("a", "b", "c")
# tuple3 = (True, False, True)
def  reverse_tuple(t):

    new_tuple = t[::-1] # [start: end : step]

    return new_tuple

def main():

    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = ("a", "b", "c")
    tuple3 = (True, False, True)

    test = [reverse_tuple(tuple1),
            reverse_tuple(tuple2),
            reverse_tuple(tuple3)]

    for t in test:
        print(t)

main()