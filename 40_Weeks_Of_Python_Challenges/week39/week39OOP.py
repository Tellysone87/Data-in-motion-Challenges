# Date: 6/26/2023
# Author: Shantel Williams
# instructions:
# Create a class called “BankAccount” that represents a bank account. The class should have the following attributes:
# 
# account_holder: A string representing the account holder’s name.
# balance: A floating-point number representing the current balance in the account.
# The class should have the following methods:
# 
# deposit(amount): A method that takes a parameter amount (a positive floating-point number) and adds it to the account’s balance.
# withdraw(amount): A method that takes a parameter amount (a positive floating-point number) and subtracts it from the account’s balance. Make sure to check if the account has sufficient balance before allowing the withdrawal.
# display_balance(): A method that displays the account holder’s name and current balance.

class BankAccount: # Represents a bank account
    def __init__(self, account_holder, balance): # initilizing. This lets us know what attibutes each Bank Account instance will contain(account_holder,balance)

        self.account_holder = account_holder # each attribute will call the value for that particular instance. That is why we us the self attribute
        self.balance = balance # holds account balance 

    def deposit(self,amount):
        """A method that takes a parameter amount (a positive floating-point number) and adds it to the account's balance."""
        
        self.balance = self.balance + amount # takes the instances balance and adds the deposit amount
        return f"+${amount} = ${self.balance}" # return the balance

    def withdraw(self, amount):
        """A method that takes a parameter amount (a positive floating-point number) and subtracts it from the account's balance. 
        Make sure to check if the account has sufficient balance before allowing the withdrawal."""

        withdrawal = amount # set amount the the variable withdrawal
        if self.balance > withdrawal: # check if amount is available
            self.balance -= withdrawal # subtract the withdrawal amount
            return f"-${withdrawal } = ${self.balance}" # return new balance 
        else:
            return f"Cannot withdraw ${withdrawal}. Insufficient funds you have a balance of ${self.balance}" # if that amount is not available, send a message with the amount available 

    def display_balance(self):
        """ A method that displays the account holder's name and current balance."""
        return f"{self.account_holder} ${self.balance}"
    
    
def grabName():
    """ function to grab the users name"""
    name = input("Please enter your name: ")

    return name
    
def main():
    name1 = grabName()
    user1 = BankAccount(name1,120.00) # quick test of class
    print(user1.display_balance())
    print(user1.deposit(50.00))
    print(user1.withdraw(100.00))
    print(user1.withdraw(80.00))

main()