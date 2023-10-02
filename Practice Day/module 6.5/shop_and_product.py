class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to the shop.")

    def buy_product(self, product_name):
        for product in self.products:
            if product.name == product_name and product.stock > 0:
                product.stock -= 1
                print(f"Congratulations! You have successfully bought {product_name}.")
                return
        print(f"Sorry, {product_name} is not available in the shop or out of stock.")

# Example usage:
product1 = Product(1, "Laptop", 1000, 5)
product2 = Product(2, "Phone", 500, 10)
product3 = Product(3, "Tablet", 300, 3)

shop = Shop()
shop.add_product(product1)
shop.add_product(product2)
shop.add_product(product3)

shop.buy_product("Phone")  # Buying a phone
shop.buy_product("Phone")  # Buying another phone
shop.buy_product("Desktop")  # Trying to buy a non-existent product
