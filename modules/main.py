from supplement import PriceError, Product
from discount import PercentageDiscount, FixedAmountDiscount
from paymentprocessor import CreditCardProcessor, PayPalProcessor, BankTransferProcessor
from cart import Cart
from logging import LogMixin
from fraction import Fraction
from product import Product  # Необходим для корректного импорта

def main():
    # Работа с продуктами и корзиной
    try:
        # Создание экземпляров класса Product
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
        # Применение различных типов скидок
        percentage_discount = PercentageDiscount(0.10)  # 10%
        fixed_amount_discount = FixedAmountDiscount(100)
        cart.apply_discount(percentage_discount)
        cart.apply_discount(fixed_amount_discount)
    except (TypeError, ValueError) as e:
        print(e)

    print(cart)
    print("Total cost after percentage discount:", cart.total_cost())
    print("Total cost after fixed amount discount:", cart.total_cost())

    # Использование различных систем оплаты
    credit_card_processor = CreditCardProcessor("1234-5678-9876-5432", "John Doe", "123", "12/25")
    paypal_processor = PayPalProcessor("john.doe@example.com")
    bank_transfer_processor = BankTransferProcessor("987654321", "John Doe")

    cart.pay(credit_card_processor)
    cart.pay(paypal_processor)
    cart.pay(bank_transfer_processor)

    # Примеры использования протокола последовательности
    for product, quantity in cart:
        print(f'Product: {product}, Quantity: {quantity}')

    print(f'First product in cart: {cart[0]}')  # Должен вывести первый элемент
    print(f'Total products in cart: {len(cart)}')  # Должен вывести количество продуктов

    # Работа с дробями
    frac1 = Fraction(1, 2)
    frac2 = Fraction(3, 4)
    print(f'Fraction 1: {frac1}')
    print(f'Fraction 2: {frac2}')

    print(f'Addition: {frac1 + frac2}')
    print(f'Subtraction: {frac1 - frac2}')
    print(f'Multiplication: {frac1 * frac2}')
    print(f'Division: {frac1 / frac2}')

    print(f'Fraction 1 == Fraction 2: {frac1 == frac2}')
    print(f'Fraction 1 != Fraction 2: {frac1 != frac2}')
    print(f'Fraction 1 < Fraction 2: {frac1 < frac2}')
    print(f'Fraction 1 <= Fraction 2: {frac1 <= frac2}')
    print(f'Fraction 1 > Fraction 2: {frac1 > frac2}')
    print(f'Fraction 1 >= Fraction 2: {frac1 >= frac2}')

    # Использование LogMixin
    log_mixin = LogMixin()
    log_mixin.log_info("This is an info message")
    log_mixin.log_warning("This is a warning message")
    log_mixin.log_error("This is an error message")
    log_mixin.log_critical("This is a critical message")

if __name__ == "__main__":
    main()
