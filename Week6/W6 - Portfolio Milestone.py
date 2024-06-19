class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self):
        class ItemToPurchase:
            item_name = "none"
            item_description = "none"
            item_price = 0
            item_quantity = 0
        item = ItemToPurchase()
        self.cart_items.append(item)

        item_name = input("\nPlease enter the name of the item you are purchasing: ")
        self.cart_items[len(self.cart_items) - 1].item_name = item_name

        item_description = input(f"Please describe these {item_name}: ")
        self.cart_items[len(self.cart_items) - 1].item_description = item_description

        while self.cart_items[len(self.cart_items) - 1].item_price <= 0:
            try:
                item_price = float(input(f"Please enter the price of {item_name} you are purchasing: $"))
                self.cart_items[len(self.cart_items) - 1].item_price = item_price
            except:
                print("Invalid entry.  Please enter a real number greater than zero.")
        while self.cart_items[len(self.cart_items) - 1].item_quantity <= 0:
            try:
                item_quantity = int(input(f"Please enter the quantity of {item_name} you are purchasing: "))
                self.cart_items[len(self.cart_items) - 1].item_quantity = item_quantity
            except:
                print("Invalid entry.  Please enter a whole number greater than zero.")

    def remove_item(self):
        if len(self.cart_items) == 0:
            print("Your shopping cart is empty.  There are no items to remove.")
        else:
            print("The current contents of your shopping cart are:")
            available_items = []
            for item in self.cart_items:
                available_items.append(item.item_name)
                print(f"\t{item.item_name}")
            item_to_remove = input("Please enter the name of the item you wish to remove: ")

            if item_to_remove in available_items:
                index_of_item = available_items.index(item_to_remove)
                del self.cart_items[index_of_item]
            else:
                print("Item not found in cart.")

    def modify_item(self, action):
        class ItemToPurchase:  # why were we asked to add this here?
            item_name = "none"
            item_description = "none"
            item_price = 0
            item_quantity = 0

        if len(self.cart_items) == 0:
            print("Your shopping cart is empty.  There are no items to modify.")
        else:
            print("The current contents of your shopping cart are:")
            available_items = []
            for item in self.cart_items:
                available_items.append(item.item_name)
                print(f"\t{item.item_name}")
            item_to_modify = input("Please enter the name of the item you wish to modify: ")

            if item_to_modify in available_items:
                index_of_item = available_items.index(item_to_modify)
                print(f"{self.cart_items[index_of_item].item_name} | Description: {self.cart_items[index_of_item].item_description}")
                print(f"You currently have {self.cart_items[index_of_item].item_quantity} in your cart with a price of ${self.cart_items[index_of_item].item_price:,.2f}")
                if action == 'quantity':
                    while True:
                        try:
                            new_quantity = int(input(f"Please enter the new desired quantity of {self.cart_items[index_of_item].item_name}: "))
                            self.cart_items[index_of_item].item_quantity = new_quantity
                            break
                        except:
                            print("Invalid entry.  Please enter a whole number greater than zero.")
                elif action == 'price':
                    print("NOT BUILT YET - Modify Price")
                elif action == 'description':
                    print("NOT BUILT YET - Modify Description")
                else:
                    print("Invalid action passed to modify_item.")
            else:
                print("Item not found in cart.")

    def get_num_items_in_cart(self):
        items = 0
        for item in self.cart_items:
            items += item.item_quantity
        return items

    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += item.item_quantity * item.item_price
        return cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY.")
        else:
            print(f"\n{self.customer_name}'s Shopping Chart - {self.current_date}")
            print(f"Number of items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"\t{item.item_name} {item.item_quantity:,} @ ${item.item_price:,.2f} = ${item.item_quantity * item.item_price:,.2f}")
            print(f"Total: ${self.get_cost_of_cart():,.2f}")

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY.")
        else:
            print(f"\n{self.customer_name}'s Shopping Chart - {self.current_date}\nItem Descriptions:")
            for item in self.cart_items:
                print(f"\t{item.item_name}: {item.item_description}")


def print_menu(shopping_cart, menu):
    user_input = input(f"\n{shopping_cart.customer_name}'s Shopping Chart - {shopping_cart.current_date}\n{menu}")
    return user_input


def main():
    user_name = input("What is your name? ")
    todays_date = input("What is today's date? ")
    shopping_cart = ShoppingCart(user_name, todays_date)
    menu = """  -------MENU-------
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: """

    while True:
        user_input = str(print_menu(shopping_cart, menu)).lower()
        if user_input == 'a':  # Add item to cart
            shopping_cart.add_item()
        elif user_input == 'r':  # Remove item from cart
            shopping_cart.remove_item()
        elif user_input == 'c':  # Change item quantity
            shopping_cart.modify_item("quantity")
        elif user_input == 'i':  # Output items' descriptions
            shopping_cart.print_descriptions()
        elif user_input == 'o':  # Output shopping cart
            shopping_cart.print_total()
        elif user_input == 'q':  # Quit
            print("\nThanks for shopping!  Have a magnanimous day!")
            break
        else:
            print("Invalid")


main()
