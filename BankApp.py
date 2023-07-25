# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:35:53 2021

@author: yusuf
"""

from BankAccount import *
def readCustomers(filename):
    file = open(filename, "r")
    liste = []
    for i in file:
        i = i.strip()
        val = i.split(",")
        Account = SavingsAccount(int(val[0]), int(val[1]), float(val[2]))
        liste.append(Account)

    return liste


def findCustomerIndex(SavingAccounts, number):
    for index in range(len(SavingAccounts)):
        if SavingAccounts[index].get_account() == number:
            return index
        


def make_operations(filename, checking):
    file = open(filename, "r")
    for i in file:
        i = i.strip()
        val = i.split(";")

        index = findCustomerIndex(checking, int(val[0]))
        checking[index].add_interest()

        if val[1] == 'W':
            checking[index].withdraw(int(val[2]))
        elif val[1] == 'D':
            checking[index].deposit(int(val[2]))
        elif val[1] == "T":
            checking[index].transfer(int(val[2]), int(val[3]))


    return checking


checking = readCustomers("customer.txt")
checking = make_operations("account.txt", checking)

print(checking)