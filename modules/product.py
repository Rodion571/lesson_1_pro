from supplement import PriceError

class Product:
    def __init__(self, name: str, price: float, description: str):
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be a number')
        if price <= 0:
            raise PriceError(price, 'Price must be positive')

        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'{self.name} - ${self.price} UAH'
