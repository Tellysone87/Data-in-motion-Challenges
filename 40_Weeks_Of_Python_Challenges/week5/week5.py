 # Date: 10/5/2023
 # Author: Shantel Williams

# Create a function that takes in a current mood and return a sentence in the following format: 
# “Today, I am feeling {mood}”. However, if no argument is passed, return “Today, I am feeling neutral”.

def feeling(mood="neutral"): # sets default value
    return f"Today, I am feeling {mood}"
   

def main():
    test = [
        feeling(),
        feeling("Happy"),
        feeling("Excited")
    ]

    for t in test:
        print(t)

main()