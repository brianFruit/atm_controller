# Author: Brian Xia

import sys
from datetime import datetime


class Card:
    def __init__(self, customer_name, card_number, expiration_date, card_type, security_code):
        self.customer_name = customer_name
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.card_type = card_type
        self.security_code = security_code


class Account:
    def __init__(self, account_balance, account_descriptor):
        self.account_balance = account_balance
        self.account_descriptor = account_descriptor
        self.transactions = []

    def deposit(self, amount, description):
        self.account_balance += amount
        self.transactions.append((datetime.now(), description, amount))
        return True

    def withdraw(self, amount, description):
        if self.account_balance < amount:
            print("WARNING: insufficient fund to withdraw, no action taken.")
            return False
        self.account_balance -= amount
        self.transactions.append((datetime.now(), description, -1 * amount))
        return True

    def check_balance(self):
        return self.account_descriptor, self.account_balance

    def list_transactions(self):
        return self.transactions


class CashBin:
    def __init__(self):
        # To be implemented by others
        pass

    def count_cash(self):
        # Hardcoded amount to be replaced by cash counter machine output
        amount = 20
        return amount


class ATMManager:
    def __init__(self):
        if not self.run_hardware_test():
            # raise appropriate error
            sys.exit(1)

        self._is_card_inserted = False
        self._is_authorized = False
        self._current_card = None
        self._current_account = None
        self._cashbin = CashBin()
    
    def insert_card(self, card, pin):
        self._is_card_inserted = True
        self._is_authorized, account = self.authorize_card(card, pin)
        if self._is_authorized:
            self._current_account = account
            self._current_card = card
        else:
            self.eject_card()

    def eject_card(self):
        self._is_card_inserted = False
        self._is_authorized = False
        self._current_card = None
        self._current_account = None

    def authorize_card(self, card, pin):
        # Connect bank API here to authorize user based on card info and pin
        account = [Account(0, 'Checking'), Account(100, 'Saving')]
        return True, account

    def deposit_cash(self, account_descriptor):
        amount = self._cashbin.count_cash()
        for acc in self._current_account:
            if acc.account_descriptor == account_descriptor:
                return acc.deposit(amount, 'cash deposit')
        return False

    def withdraw_cash(self, account_descriptor, amount):
        for acc in self._current_account:
            if acc.account_descriptor == account_descriptor:
                return acc.withdraw(amount, 'cash withdrawal')
        return False

    def check_balance(self, account_descriptor):
        if self._current_account is not None:
            for acc in self._current_account:
                if acc.account_descriptor == account_descriptor:
                    return acc.account_balance
        return False

    def run_hardware_test(self):
        # Add hw tests
        return True

    def get_all_accounts(self):
        # For UI team to show account and balance
        return self._current_account

    def get_customer_name(self):
        # For UI team to show cusomter greetings
        if self._current_card is not None:
            return self._current_card.customer_name
        else:
            return None


if __name__ == '__main__':
    atm = ATMManager()
    card = Card('Brian', '0000000000000000', '10/30/2020', 'debit', 123)
    atm.insert_card(card, 4321)

    print("Welcome %s" % atm.get_customer_name())

    print("Before deposit: %s" % atm.check_balance("Checking"))
    atm.deposit_cash('Checking')
    atm.deposit_cash('Checking')
    print("After deposit of $20 twice: %s" % atm.check_balance("Checking"))
    assert atm.check_balance("Checking") == (20 + 20)

    print("Before withdrawal: %s" % atm.check_balance("Saving"))
    atm.withdraw_cash('Saving', 99)
    print("After withdrawal of $99: %s" % atm.check_balance("Saving"))
    assert atm.check_balance("Saving") == (100 - 99)

    atm.eject_card()
    assert atm.get_all_accounts() == None
    assert atm.get_customer_name() == None

    
    



