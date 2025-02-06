from product import Product
from inventory import Inventory

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = Inventory()

    def add_product(self, product_id, name, quantity):
        product = Product(product_id, name, quantity)
        return self.inventory.add_product(product)

    def list_products(self):
        return self.inventory.list_products()

    def update_product_quantity(self, product_id, quantity):
        product = self.inventory.find_product(product_id)
        if product:
            return product.update_quantity(quantity)
        return "Product not found."