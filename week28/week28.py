# Date: 8/31/2023
# Author: Shantel Williams

# The vertical bar | is the equivalent to “or” in RegEx. The regular expression x | y matches either “x” or “y”. 
# Write the regular expression that will match all red flag and blue flag in a string. You must use | in your expression. Flags can come in any order.

# Examples:

# txt1 = “red flag blue flag”
# txt2 = “yellow flag red flag blue flag green flag”
# txt3 = “pink flag red flag black flag blue flag green flag red flag”
# pattern = “yourregularexpressionhere”

# re.findall(pattern, txt1) ➞ [“red flag”, “blue flag”]
# re.findall(pattern, txt2) ➞ [“red flag”, “blue flag”]
# re.findall(pattern, txt3) ➞ [“red flag”, “blue flag”, “red flag”]
import regex as re

def main():
    txt1 = "red flag blue flag"
    txt2 = "yellow flag red flag blue flag green flag"
    txt3 = "pink flag red flag black flag blue flag green flag red flag"
    pattern = "red flag|blue flag"

    test =  [
            re.findall(pattern, txt1),
            re.findall(pattern, txt2),
            re.findall(pattern, txt3)
            ]

    for tests in test:
        print(tests)

main()