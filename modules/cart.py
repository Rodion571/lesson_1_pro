from logging import LogMixin
from product import Product
from discount import Discount
from paymentprocessor import PaymentProcessor

class DiscountMixin:
    def apply_discount(self, discount: Discount):
        if hasattr(self, 'products') and self.products:  # Перевіряємо наявність продуктів
            for product in self.products:
                product.price = discount.apply(product.price)

class Cart(DiscountMixin, LogMixin):
    def __init__(self):
        LogMixin.__init__(self)
        self.products = {}

    def add_product(self, product: Product, quantity: int | float = 1):
        if not isinstance(quantity, (int, float)):
            self.log_error('Quantity must be a number')
            raise TypeError('Quantity must be a number')
        if quantity <= 0:
            self.log_error('Quantity must be positive')
            raise ValueError('Quantity must be positive')
        if not isinstance(product, Product):
            raise TypeError('Product must be an instance of the Product class')

        self.products[product] = self.products.get(product, 0) + quantity

    def total_cost(self):
        return sum(product.price * quantity for product, quantity in self.products.items())

    def pay(self, payment_processor: PaymentProcessor):
        self.log_info(f"Processing payment of {self.total_cost()} UAH with {payment_processor.__class__.__name__}")
        payment_processor.pay(self.total_cost())

    def __str__(self):
        return '\n'.join(f'{product} x {quantity} = {product.price * quantity} UAH'
                         for product, quantity in self.products.items())

    # Реалізація ітераційного протоколу
    def __iter__(self):
        """Повертаємо ітератор по продуктах та їх кількості."""
        return iter(self.products.items())

    def __getitem__(self, index):
        """Дозволяє отримувати елемент за індексом."""
        if isinstance(index, int):
            if 0 <= index < len(self.products):
                return list(self.products.items())[index]
            else:
                raise IndexError('Index out of range')
        else:
            raise TypeError('Index must be an integer')

    def __len__(self):
        """Повертає кількість унікальних продуктів у кошику."""
        return len(self.products)

    def __next__(self):
        """Додаємо метод __next__, щоб підтримувати ітерації."""
        if self._current_index < len(self.products):
            product = list(self.products.items())[self._current_index]
            self._current_index += 1
            return product
        else:
            raise StopIteration

    def reset_iterator(self):
        """Скидання ітератора для повторної ітерації."""
        self._current_index = 0
