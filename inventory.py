from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return f"Product {product.name} has been added to the inventory."

    def list_products(self):
        if self.products:
            products_list = "\n".join([f"{i + 1}. {product}" for i, product in enumerate(self.products)])
            return f"Products in the inventory:\n{products_list}"
        return "No products in the inventory."

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None