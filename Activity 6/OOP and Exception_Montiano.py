class Item:
    def __init__(self, item_id, name, description, price):
        self.id = item_id
        self.name = name
        self.description = description
        self.price = max(0, price)

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Item ID already exists.")
            return
        self.items[item_id] = Item(item_id, name, description, price)
        print("Item added.")

    def read_items(self):
        for item in self.items.values():
            print(f"{item.id}: {item.name}, {item.description}, ${item.price}")

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id in self.items:
            item = self.items[item_id]
            if name: item.name = name
            if description: item.description = description
            if price is not None: item.price = max(0, price)
            print("Item updated.")
        else:
            print("Item not found.")

    def delete_item(self, item_id):
        if self.items.pop(item_id, None):
            print("Item deleted.")
        else:
            print("Item not found.")

def main():
    manager = ItemManager()
    while True:
        choice = input("[C]reate [R]ead [U]pdate [D]elete [Q]uit: ").strip().upper()
        if choice == 'Q': break
        item_id = input("Enter Item ID: ")
        if choice == 'C':
            manager.create_item(item_id, input("Name: "), input("Description: "), float(input("Price: ")))
        elif choice == 'R':
            manager.read_items()
        elif choice == 'U':
            manager.update_item(item_id, input("New Name: ") or None, input("New Description: ") or None, float(input("New Price: ") or 0))
        elif choice == 'D':
            manager.delete_item(item_id)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()