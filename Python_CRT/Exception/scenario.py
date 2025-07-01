'''
Scenario:
Your're stimulating an ATM machine.A user inputs the amount they want to withdraw

Task:
- Raise an error if the amount is more than the account balance
- Also handle non-integer input gracefully
 '''
class InsufficientFundsError(Exception): pass
balance=10000
try:
    amount=int(input("Enter the amount to withdraw: "))
    if amount<=0:
        raise ValueError("Withdrawal amount must be greater than 0")
    if amount>balance:
        raise InsufficientFundsError("Insufficient balance for Withdrawal")
    balance-=amount
    print(f"Withdrawal successful! Reamining balance: {balance}")
except ValueError as ve:
    print("Invalid input:",ve)
except InsufficientFundsError as ie:
    print("Transcarion Failed:")