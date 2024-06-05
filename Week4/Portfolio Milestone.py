class ItemToPurchase:
    item_name = "none"
    item_price = 0
    item_quantity = 0

    def print_item_cost(self):
        print(f"{item.item_name} {item.item_quantity:,} @ ${item.item_price:,.2f} = ${item.item_quantity * item.item_price:,.2f}")

items = []
while len(items) < 2:
    item = ItemToPurchase()
    items.append(item)
    item_name = input("Please enter the name of the item you are purchasing: ")
    items[len(items)-1].item_name = item_name
    while items[len(items)-1].item_price <= 0:
        try:
            item_price = float(input(f"Please enter the price of {item_name} you are purchasing: $"))
            items[len(items) - 1].item_price = item_price
        except:
            print("Invalid entry.  Please enter a real number greater than zero.")
    while items[len(items)-1].item_quantity <= 0:
        try:
            item_quantity = int(input(f"Please enter the quantity of {item_name} you are purchasing: "))
            items[len(items) - 1].item_quantity = item_quantity
        except:
            print("Invalid entry.  Please enter a whole number greater than zero.")

total_cost = 0
for item in items:
    item.print_item_cost()
    total_cost = total_cost + (item.item_quantity * item.item_price)
print(f"Total: ${total_cost:,.2f}")
