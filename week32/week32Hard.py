# Date: 8/15/2023
# Author: Shantel Williams

# “Loves me, loves me not” is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase “Loves me” 
# and “Loves me not” when determining whether the one that they love, loves them back.
# Given a number of petals, return a string which repeats the phrases “Loves me” 
# and “Loves me not” for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

# Examples:
# loves_me(3) ➞ “Loves me, Loves me not, LOVES ME”
# loves_me(6) ➞ “Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT”
# loves_me(1) ➞ “LOVES ME”

# Notes
# Remember to return a string.
# The first phrase is always “Loves me”.

def loves_me(number_of_petals):
    """ return a string which repeats the phrases “Loves me” and “Loves me not” for every alternating petal,
      and return the last phrase in all caps. """
    stop = number_of_petals # tells the program where to stop
    list_of_phrase = []

    phrase1 = "Loves me" # the two alternating phrases
    phrase2 = "Loves me not"

    end_phrase = "" # empty string to return

    i = 1

    if number_of_petals == 0:
        return "You don't even have a flower."

    if i == number_of_petals:
        return "LOVES ME"

    for i in range(stop):
        if i % 2 == 0:
            list_of_phrase.append(phrase1)
        else:
            list_of_phrase.append(phrase2)
    
    if i == stop:
        if stop % 2 == 0:
            list_of_phrase.append("LOVES ME")
        else:
             list_of_phrase.append("LOVES ME NOT")

    list_of_phrase[-1] = list_of_phrase[-1].upper()

    end_phrase = ", ".join(list_of_phrase)


    return end_phrase

def main():
    test = loves_me(3) 
    test2 = loves_me(6) 
    test3 = loves_me(1)
    print(test)
    print(test2)
    print(test3)

main()