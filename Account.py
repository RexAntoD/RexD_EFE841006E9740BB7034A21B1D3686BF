class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        elif amount > self._account_balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be greater than zero."

    def display_balance(self):
        return f"Account balance for {self._account_holder_name}: ${self._account_balance}"

# Example usage:
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", 1000)
    print(account.display_balance())
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.withdraw(1500))
          