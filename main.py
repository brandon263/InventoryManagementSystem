from inventory_management_system import InventoryManagementSystem

def main():
    ims = InventoryManagementSystem()
    while True:
        print("\nInventory Management System Menu:")
        print("1. Add a product")
        print("2. List products")
        print("4. Find a product")
        print("5. Exit")

        choice = input("Chose action: ")
        if choice == '1':
            product_id = input("Enter the product ID: ")
            name = input("Enter the product name: ")
            quantity = int(input("Enter the quantity: "))
            print(ims.add_product(product_id, name, quantity))
        elif choice == '2':
            print(ims.list_products())
        elif choice == '3':
            product_id = input("Enter the product ID: ")
            quantity = int(input("Enter the quantity to update: "))
            print(ims.update_product_quantity(product_id, quantity))
        elif choice == '4':
            product_id = input("Enter the product ID: ")
            print(ims.find_product(product_id))
        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()