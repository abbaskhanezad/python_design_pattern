"""
Decorator Design Pattern (Structural)
Allows you to change the behavior of an object dynamically at runtime by the decorator class.
This pattern uses a combination instead of inheritance.
Decorator pattern makes it possible to add behavior to an object dynamically without changing
the behavior of other objects in the same class.
"""

TAX_RATE = {
    'USA': 0.23,
    'IR': 0.10
}

def add_tax(fn):
    def wrapper(product_object):
        country = product_object.address.country
        return fn(product_object) * (1 + TAX_RATE[country])
    return wrapper

class Product:
    def __init__(self, name, price, address):
        self.name = name
        self.price = price
        self.address = address
    
    @add_tax
    def get_price(self):
        return self.price


class Address:
    def __init__(self, country, detail):
        self.country = country
        self.detail = detail


        
if __name__ == '__main__':
    address_usa = Address('USA', 'some details...')
    address_uae = Address('IR', 'some details...')

    p1 = Product(name='Galaxy 780', price=2000, address=address_usa)
    p2 = Product(name='Galaxy ZSlide', price=3000, address=address_uae)

    print(f"Product1 => Price with tax: {p1.get_price()}")
    print(f"Product2 => Price with tax: {p2.get_price()}")
