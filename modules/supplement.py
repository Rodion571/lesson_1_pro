class PriceError(Exception):
    def __init__(self, price, message):
        super().__init__(message)
        self.price = price
        self.message = message

    def __str__(self):
        return f'Price {self.price} is invalid: {self.message}'
