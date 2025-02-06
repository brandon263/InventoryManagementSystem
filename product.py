class Product:
    def __init__(self, product_id, name, quantity):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id}: {self.name} (Quantity: {self.quantity})"

    def update_quantity(self, quantity):
        self.quantity += quantity
        return f"The quantity of {self.name} is now {self.quantity}."