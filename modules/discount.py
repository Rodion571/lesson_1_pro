class Discount:
    def apply(self, price):
        raise NotImplementedError


class PercentageDiscount(Discount):
    def __init__(self, percentage: float = 0.1):
        if not isinstance(percentage, (int, float)):
            raise TypeError('Percentage must be a number')
        if percentage < 0 or percentage > 1:
            raise ValueError('Percentage must be between 0 and 1')
        self.percentage = percentage

    def apply(self, price: float):
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be a number')
        if price < 0:
            raise ValueError('Price cannot be negative')
        return price * (1 - self.percentage)


class FixedAmountDiscount(Discount):
    def __init__(self, amount: float = 0):
        if not isinstance(amount, (int, float)):
            raise TypeError('Amount must be a number')
        if amount < 0:
            amount = 0
        self.amount = amount

    def apply(self, price: float):
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be a number')
        if price < 0:
            raise ValueError('Price cannot be negative')
        if price < self.amount:
            return 0
        return price - self.amount
