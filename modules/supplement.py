class PriceError(Exception):
    def __init__(self, price, message):
        super().__init__(message)
        self.price = price
        self.message = message

    def __str__(self):
        return f'Price {self.price} is invalid: {self.message}'
def main():
    try:
        # Creating instances of the Product class
        product1 = Product("Laptop", 1500.00, "A high-end gaming laptop")
        product2 = Product("Mouse", 50.00, "A wireless mouse")
        product3 = Product("Keyboard", 100.00, "A mechanical keyboard")
    except (PriceError, TypeError) as e:
        print(e)

    cart = Cart()
    try:
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        cart.add_product(product3, 1)
    except (TypeError, ValueError) as e:
        print(e)

    print(cart)
    print("Total cost:", cart.total_cost())

    try:
        # Applying different types of discounts
        percentage_discount = PercentageDiscount(10)
        fixed_amount_discount = FixedAmountDiscount(100)
        cart.apply_discount(percentage_discount)
        cart.apply_discount(fixed_amount_discount)
    except (TypeError, ValueError) as e:
        print(e)

    print(cart)
    print("Total cost after percentage discount:", cart.total_cost())

    print(cart)
    print("Total cost after fixed amount discount:", cart.total_cost())

    # Using different payment systems
    credit_card_processor = CreditCardProcessor("1234-5678-9876-5432", "John Doe", "123", "12/25")
    paypal_processor = PayPalProcessor("john.doe@example.com")
    bank_transfer_processor = BankTransferProcessor("987654321", "John Doe")

    cart.pay(credit_card_processor)
    cart.pay(paypal_processor)
    cart.pay(bank_transfer_processor)