import csv

def setup_environment():
    # Create an empty inventory list
    return []

# take input
def take_item_data():
    print("Enter fruit details:")
    fruit_name = input("Fruit Name: ").strip()
    unit_price = float(input("Unit Price: "))
    quantity = int(input("Quantity: "))
    total_price = unit_price * quantity
    print(f"Total Price: {total_price}\n")
    return [fruit_name, unit_price, quantity, total_price]

 
# CSV new =========================================================================================
def save_item_data(inventory, filename="inventory.csv"):
    with open(filename, 'w', newline="") as file:  # Corrected 'open' syntax
        w = csv.writer(file)
        w.writerow(["Fruit Name", "Unit Price", "Quantity", "Total Price"])
        w.writerows(inventory)
    print(f"Inventory saved to {filename}.\n")

# CSV new =========================================================================================

# Add
def add_item_to_inventory(inventory, item_data):
    # Check if the item already exists
    for item in inventory:
        if item[0].lower() == item_data[0].lower():
            item[2] += item_data[2]  # Update quantity
            item[3] = item[1] * item[2]  # Update total price
            print(f"Updated {item_data[0]} in the inventory.\n")
            return
    # Add new item if it does not exist
    inventory.append(item_data)
    print(f"Added {item_data[0]} to the inventory.\n")
    save_item_data(inventory) # CSV ========================================
    
    
# summary
def print_summary(inventory):
    if not inventory:
        print("\nInventory is empty.")
    else:
        print("\nFruit Inventory Summary:")
        print("Fruit Name      Unit Price      Quantity      Total Price")
        for item in inventory:
            print(f"{item[0]:<15} {item[1]:<15} {item[2]:<15} {item[3]:<15}")


# delete
def delete_item(inventory):
    print("\nDelete an item from inventory")
    fruit_to_delete = input("Enter the name of the fruit to delete: ").strip()
    for item in inventory:
        if item[0].lower() == fruit_to_delete.lower():
            inventory.remove(item)
            print(f"{fruit_to_delete} has been deleted from the inventory.\n")
            save_item_data(inventory) # CSV ========================================
            return
    print(f"{fruit_to_delete} not found in the inventory.\n")


# search
def search_item(inventory):
    print("\nSearch for an item in inventory")
    fruit_to_search = input("Enter the name of the fruit to search: ").strip()
    for item in inventory:
        if item[0].lower() == fruit_to_search.lower():
            print("\nFruit Found:")
            print("Fruit Name      Unit Price      Quantity      Total Price")
            print(f"{item[0]:<15} {item[1]:<15} {item[2]:<15} {item[3]:<15}")
            return
    print(f"{fruit_to_search} not found in the inventory.\n")



# main 1st
def main():
    inventory = setup_environment()

    while True:
        print("\nOptions:")
        print("1. Add a new item")
        print("2. View inventory summary")
        print("3. Delete an item")
        print("4. Search for an item")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            item_data = take_item_data()
            add_item_to_inventory(inventory, item_data)
        elif choice == "2":
            print_summary(inventory)
        elif choice == "3":
            delete_item(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
