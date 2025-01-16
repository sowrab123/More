import csv

class Inventory:
    def __init__(self, filename="inventory.csv"):
        self.filename = filename
        self.inventory = []

    def save_to_csv(self):
        """Save the inventory to a CSV file."""
        with open(self.filename, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Fruit Name", "Unit Price", "Quantity", "Total Price"])
            writer.writerows(self.inventory)
        print(f"Inventory saved to {self.filename}.")

    def add_item(self, fruit_name, unit_price, quantity):
        """Add a new item or update an existing item in the inventory."""
        for item in self.inventory:
            if item[0].lower() == fruit_name.lower():
                item[2] += quantity  # Update quantity
                item[3] = item[1] * item[2]  # Update total price
                print(f"Updated {fruit_name} in the inventory.")
                self.save_to_csv()
                return
        # Add new item if it does not exist
        total_price = unit_price * quantity
        self.inventory.append([fruit_name, unit_price, quantity, total_price])
        print(f"Added {fruit_name} to the inventory.")
        self.save_to_csv()

    def delete_item(self, fruit_name):
        """Delete an item from the inventory."""
        for item in self.inventory:
            if item[0].lower() == fruit_name.lower():
                self.inventory.remove(item)
                print(f"{fruit_name} has been deleted from the inventory.")
                self.save_to_csv()
                return
        print(f"{fruit_name} not found in the inventory.")

    def search_item(self, fruit_name):
        """Search for an item in the inventory."""
        for item in self.inventory:
            if item[0].lower() == fruit_name.lower():
                print("\nFruit Found:")
                print("Fruit Name      Unit Price      Quantity      Total Price")
                print(f"{item[0]:<15} {item[1]:<15} {item[2]:<15} {item[3]:<15}")
                return
        print(f"{fruit_name} not found in the inventory.")

    def display_inventory(self):
        """Display the entire inventory."""
        if not self.inventory:
            print("\nInventory is empty.")
        else:
            print("\nFruit Inventory Summary:")
            print("Fruit Name      Unit Price      Quantity      Total Price")
            for item in self.inventory:
                print(f"{item[0]:<15} {item[1]:<15} {item[2]:<15} {item[3]:<15}")

class InventoryApp:
    def __init__(self):
        self.inventory = Inventory()

    def take_item_data(self):
        """Prompt the user to input item details."""
        print("Enter fruit details:")
        fruit_name = input("Fruit Name: ").strip()
        unit_price = float(input("Unit Price: "))
        quantity = int(input("Quantity: "))
        return fruit_name, unit_price, quantity

    def menu(self):
        """Display the menu and handle user input."""
        while True:
            print("\nOptions:")
            print("1. Add a new item")
            print("2. View inventory summary")
            print("3. Delete an item")
            print("4. Search for an item")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                fruit_name, unit_price, quantity = self.take_item_data()
                self.inventory.add_item(fruit_name, unit_price, quantity)
            elif choice == "2":
                self.inventory.display_inventory()
            elif choice == "3":
                fruit_name = input("Enter the name of the fruit to delete: ").strip()
                self.inventory.delete_item(fruit_name)
            elif choice == "4":
                fruit_name = input("Enter the name of the fruit to search: ").strip()
                self.inventory.search_item(fruit_name)
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = InventoryApp()
    app.menu()
