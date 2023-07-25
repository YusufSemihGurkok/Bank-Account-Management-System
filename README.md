## Bank Account Management System
This Python program implements a Bank Account Management System that allows users to manage bank accounts, make deposits, withdrawals, and transfers, and calculate interest for savings accounts.

## Features
BankAccount Class: The BankAccount class represents a generic bank account with attributes such as account number and balance. It provides methods to deposit, withdraw, and transfer money between accounts.
SavingsAccount Class: The SavingsAccount class inherits from the BankAccount class and includes an additional attribute for interest rate. It also provides a method to add interest to the account balance.
readCustomers Function: The program includes a function called readCustomers that reads customer information from an input file (customer.txt) and creates a list of SavingsAccount objects based on the data in the file.
make_operations Function: The program includes a function called make_operations that reads operations from an input file (account.txt) and performs the corresponding operations (e.g., deposit, withdrawal, transfer, and interest calculation) on the accounts in the list.
## Prerequisites
Python 3.x
## How to Use
Clone the repository or download the BankAccount.py and main.py files.

Prepare the input data files (customer.txt and account.txt) in the following formats:

customer.txt:
accountNumber,balance,rate
123,1000,0.02
456,2000,0.03
... (Add more accounts)

account.txt:
accountNumber;operation;amount;transferTo (if applicable)
123;W;500;
456;D;1000;
123;T;200;456
... (Add more operations)
Run the Python script main.py.

The program will read customer information from customer.txt, perform the operations listed in account.txt, and display the updated account balances.

## License
This project is licensed under the MIT License.
