class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price:.2f}, Description: {self.description}"
class Cart:
    def __init__(self):
        self.items = {}  # Словник для зберігання товарів і їх кількості
    def add_product(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    def total_cost(self):
        return sum(product.price * quantity for product, quantity in self.items.items())
    def __str__(self):
        cart_contents = '\n'.join([f"{product.name} (x{quantity}) - {product.price * quantity:.2f}" for product, quantity in self.items.items()])
        return f"Cart contents:\n{cart_contents}\nTotal cost: {self.total_cost():.2f}"
product1 = Product("Laptop", 1500.00, "High performance laptop")
product2 = Product("Mouse", 25.00, "Wireless mouse")
product3 = Product("Keyboard", 45.00, "Mechanical keyboard")
cart = Cart()
cart.add_product(product1, 1)
cart.add_product(product2, 2)
cart.add_product(product3, 1)
print(cart)
