class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number, card_holder, cvv, expiry_date):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount):
        print(f'Paying ${amount} with credit card {self.card_number}')


class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f'Paying ${amount} with PayPal account {self.email}')


class BankTransferProcessor(PaymentProcessor):
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder

    def pay(self, amount):
        print(f'Paying ${amount} with bank transfer from account {self.account_number}')