class Product:
    """
    Class for product representation.
    """

    def __init__(self, name: str, price: int | float, currency='UAH'):
        self.name = name
        self.price = price
        self.currency = currency

    def __str__(self):
        return f'{self.name}: {self.price:.2f} {self.currency}'


class PaymentProcessor:
    def pay(self, amount: float):
        """
        Метод для оплати. Має бути перевизначений у підкласах.

        Parameters:
        amount (float): Сума для оплати.

        Returns:
        None
        """
        raise NotImplementedError("Метод pay повинен бути реалізований у підкласах")


class Discount:
    def apply(self, amount: float):
        """
        Метод для застосування дисконту. Має бути перевизначений у підкласах.

        Parameters:
        amount (float): Початкова сума.

        Returns:
        float: Сума після застосування дисконту.
        """
        raise NotImplementedError("Метод apply повинен бути реалізований у підкласах")


class PercentageDiscount(Discount):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply(self, amount: float):
        """
        Реалізація дисконту у вигляді відсотка.

        Parameters:
        amount (float): Початкова сума.

        Returns:
        float: Сума після застосування дисконту.
        """
        discount_amount = amount * (self.percentage / 100)
        return amount - discount_amount


class FixedAmountDiscount(Discount):
    def __init__(self, discount_amount: float):
        self.discount_amount = discount_amount

    def apply(self, amount: float):
        """
        Реалізація фіксованої знижки.

        Parameters:
        amount (float): Початкова сума.

        Returns:
        float: Сума після застосування дисконту.
        """
        return max(amount - self.discount_amount, 0)


class DiscountMixin:
    def apply_discount(self, discount: Discount):
        """
        Застосовує дисконт до всіх товарів у кошику.

        Parameters:
        discount (Discount): Інстанс класу дисконтів.

        Returns:
        None
        """
        for product, quantity in self._Cart__products.items():
            original_price = product.price
            discounted_price = discount.apply(original_price)
            product.price = discounted_price


class Cart(DiscountMixin):
    """
    Class for cart representation.
    """

    def __init__(self):
        self._Cart__products = {}

    def add_product(self, product: Product, quantity: int | float = 1):
        self._Cart__products[product] = self._Cart__products.get(product, 0) + quantity

    def total(self):
        return sum(product.price * quantity for product, quantity in self._Cart__products.items())

    def pay(self, payment_processor: PaymentProcessor):
        """
        Метод для здійснення оплати за допомогою наданого процесора оплати.

        Parameters:
        payment_processor (PaymentProcessor): Інстанс процесора оплати.

        Returns:
        None
        """
        amount = self.total()
        payment_processor.pay(amount)

    def __str__(self):
        return '\n'.join([f'{product} x {quantity} = {product.price * quantity:.2f} {product.currency}'
                          for product, quantity in self._Cart__products.items()])


class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount: float):
        """
        Реалізація оплати кредитною карткою.

        Parameters:
        amount (float): Сума для оплати.

        Returns:
        None
        """
        print(f"Оплата кредитною карткою на суму {amount:.2f} UAH")


class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float):
        """
        Реалізація оплати через PayPal.

        Parameters:
        amount (float): Сума для оплати.

        Returns:
        None
        """
        print(f"Оплата через PayPal на суму {amount:.2f} UAH")


class BankTransferProcessor(PaymentProcessor):
    def pay(self, amount: float):
        """
        Реалізація оплати банківським переказом.

        Parameters:
        amount (float): Сума для оплати.

        Returns:
        None
        """
        print(f"Оплата банківським переказом на суму {amount:.2f} UAH")


if __name__ == '__main__':
    cart = Cart()
    cart.add_product(Product('Bread', 10))
    cart.add_product(Product('Milk', 20))
    cart.add_product(Product('Butter', 30))
    print(cart)
    print(f'Total: {cart.total()} UAH')

    # Застосування знижки
    discount = PercentageDiscount(10)  # 10% знижка
    cart.apply_discount(discount)

    # Використання одного з платіжних процесорів для оплати
    payment_method = CreditCardProcessor()
    cart.pay(payment_method)