# Shantel Williams
# 11/29/2023

# Medium Challenge: Password Strength Checker
# Write a function password_strength(password) that takes a string password as input and returns a message describing its strength: “Weak”, “Moderate”, or “Strong”.

# A “Weak” password is one that is less than 8 characters long.
# A “Moderate” password is one that is at least 8 characters long but does not contain both letters and numbers.
# A “Strong” password is one that is at least 8 characters long and contains both letters and numbers.

# Letters can be checked in Python String using the isalpha() method and numbers can be checked using the isdigit() method.
def password_strength(password):
    check = {"number": "", "letter": ""}

# A “Weak” password is one that is less than 8 characters long.
    if len(password) < 8:
        return "Weak"
    
    for char in password:
        if char.isalpha():
            check["letter"] = "True"
        if char.isdigit():
            check["number"] = "True"

# A “Strong” password is one that is at least 8 characters long and contains both letters and numbers.
    if check["letter"] == "True" and check["number"] == "True":
        return "Strong"
    else: # A “Moderate” password is one that is at least 8 characters long but does not contain both letters and numbers.
        return "Moderate"

def main():
    print(password_strength("short")) # Output: "Weak"
    print(password_strength("longerOne")) # Output: "Moderate"
    print(password_strength("longerOne1")) # Output: "Strong"

main()