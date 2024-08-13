class InvalidPriceError(Exception):
    """Виключення, що виникає, коли ціна продукту недійсна."""
    def __init__(self, price):
        super().__init__(f"Invalid price: {price}. Price must be greater than zero.")
        self.price = price

class InvalidQuantityError(Exception):
    """Виключення, що виникає, коли кількість продукту недійсна."""
    def __init__(self, quantity):
        super().__init__(f"Invalid quantity: {quantity}. Quantity must be greater than zero.")
        self.quantity = quantity

class Product:
    def __init__(self, name, price, description):
        self.name = name
        try:
            if price > 0:
                self.price = price
                print('Nice. You entered the price correctly.')
            else:
                raise InvalidPriceError(price)
        except InvalidPriceError as e:
            print(e)
            self.price = 0

        self.description = description

    def __str__(self):
        return f'{self.name} - ${self.price} UAH'

class Discount:
    def apply(self, price):
        pass

class PercentageDiscount(Discount):
    def __init__(self, percentage: float | int = 0.1):
        if 0 <= percentage <= 1:
            self.percentage = percentage
        else:
            self.percentage = 0

    def apply(self, price: float | int):
        return price * (1 - self.percentage)

class FixedAmountDiscount(Discount):
    def __init__(self, amount: float | int = 0):
        if amount < 0:
            amount = 0
        self.amount = amount

    def apply(self, price: float | int):
        if price < self.amount:
            return 0
        return price - self.amount

class DiscountMixin:
    def apply_discount(self, discount: Discount):
        # if self.products not exists
        if hasattr(self, 'products'):
            for product in self.products:
                product.price = discount.apply(product.price)

class PaymentProcessor:
    def pay(self, amount):
        pass

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

class Cart(DiscountMixin):
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            raise InvalidQuantityError(quantity)
        self.products[product] = self.products.get(product, 0) + quantity

    def total_cost(self):
        return sum(product.price * quantity for product, quantity in self.products.items())

    def pay(self, payment_processor: PaymentProcessor):
        payment_processor.pay(self.total_cost())

    def __str__(self):
        return '\n'.join(f'{product} x {quantity} = {product.price * quantity} UAH'
                         for product, quantity in self.products.items())

def main():
    try:
        # Creating instances of the Product class
        product1 = Product("Laptop", -2, "A high-end gaming laptop")
        product2 = Product("Mouse", 50.00, "A wireless mouse")
        product3 = Product("Keyboard", 100.00, "A mechanical keyboard")

        # Creating an instance of the Cart class and adding products
        cart = Cart()
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        cart.add_product(product3, 0)  # Некоректна кількість, викликає виключення
    except (InvalidPriceError, InvalidQuantityError) as e:
        print(e)

    print(cart)
    print("Total cost:", cart.total_cost())

    # Applying different types of discounts
    percentage_discount = PercentageDiscount(10)
    fixed_amount_discount = FixedAmountDiscount(100)

    cart.apply_discount(percentage_discount)
    print(cart)
    print("Total cost after percentage discount:", cart.total_cost())

    cart.apply_discount(fixed_amount_discount)
    print(cart)
    print("Total cost after fixed amount discount:", cart.total_cost())

    # Using different payment systems
    credit_card_processor = CreditCardProcessor("1234-5678-9876-5432", "John Doe", "123", "12/25")
    paypal_processor = PayPalProcessor("john.doe@example.com")
    bank_transfer_processor = BankTransferProcessor("987654321", "John Doe")

    cart.pay(credit_card_processor)
    cart.pay(paypal_processor)
    cart.pay(bank_transfer_processor)

if __name__ == "__main__":
    main()
