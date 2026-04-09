from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 1000, 5)
p2 = Product("Telefon", 500, 10)
p3 = Product("Tablet", 300, 7)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.display_products()
print("Ukupna vrednost:", manager.total_value())
from cart import Cart
import random

cart = Cart()

random_products = random.sample(manager.products, 3)

for p in random_products:
    cart.add_to_cart(p)

cart.display_cart()
print("Ukupno za naplatu:", cart.total_price())