# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:35:50 2021

@author: yusuf
"""

class BankAccount():
    def __init__(self,a_number):
        self.__a_number=a_number
        self.__balance=0
    def get_account(self):
        return self.__a_number
    def deposit(self,deposit):
        self.__balance += deposit
        return self.__balance
    def withdraw(self,amount):
        if self.__balance> amount:
            self.__balance -= amount
            return True
        else:
            print("There is not enough money!")
            print(amount , " TL cannot be withdrawn from account", self.__a_number)
            return False
    def transfer(self,amount, other):
        if self.__balance>amount:
            self.__balance -=amount
        # if self.__balance> amount:
        #     self.withdraw(amount)
        #     other.deposit(amount)
            


    def __repr__(self):

        output = "\nAccount Number: " + str(self.__a_number) + "\nBalance: " + str(self.__balance) + " TL"
        return output

class SavingsAccount(BankAccount):
    def __init__(self,a_number,balance,rate):
        BankAccount. __init__(self,a_number)
        self.__balance=balance
        self.__rate=rate
        
        
    def add_interest(self):
        rated =self.__balance*self.__rate
        self.__balance+=rated
        return self.__balance