from abc import ABC, abstractmethod


# ==========================================
#          ABSTRACT PARENT CLASS
# ==========================================

class MenuItem(ABC):

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Price cannot be negative.")

    # Abstract method
    @abstractmethod
    def display_item(self):
        pass


# ==========================================
#              FOOD SUBCLASS
# ==========================================

class Food(MenuItem):

    def display_item(self):
        print(f"{self.name} - ₱{self.get_price():.2f}")


# ==========================================
#             DRINK SUBCLASS
# ==========================================

class Drink(MenuItem):

    def display_item(self):
        print(f"{self.name} - ₱{self.get_price():.2f}")


# ==========================================
#              MANG INASAL MENU
# ==========================================

menu_items = [
    Food("Chicken Inasal - Paa", 99),
    Food("Chicken Inasal - Pecho", 120),
    Food("Pork BBQ", 85),
    Food("Palabok", 75),
    Food("Halo-Halo", 65),
    Food("Liempo Inasal", 150),
    Food("Pork Sisig", 100),
    Food("Extra Rice", 25),
    Drink("Iced Tea", 45),
    Drink("Coke", 40),
    Drink("Sprite", 40),
    Drink("Royal", 40)
]


# ==========================================
#             DISPLAY MENU
# ==========================================

def display_menu():

    print("\n================================")
    print("        MANG INASAL MENU")
    print("================================")

    for number, item in enumerate(menu_items, start=1):
        print(f"{number}. ", end="")
        item.display_item()

    print("0. Proceed to Payment")


# ==========================================
#              TAKE ORDER
# ==========================================

def take_order():

    cart = []

    while True:

        display_menu()

        # Ask for item choice
        try:
            choice = int(input("\nSelect an item: "))

        except ValueError:
            print("\n❌ Invalid input!")
            print("Please enter a number.")
            continue

        # ==================================
        #       PROCEED TO PAYMENT
        # ==================================

        if choice == 0:

            if len(cart) == 0:
                print("\n❌ Your cart is empty!")
                print("Please select an item first.")
                continue

            break

        # ==================================
        #       CHECK ITEM CHOICE
        # ==================================

        if choice < 1 or choice > len(menu_items):

            print("\n❌ Invalid choice!")
            print("Please select an item from the menu.")
            continue

        # Get selected item
        selected_item = menu_items[choice - 1]

        # ==================================
        #          ASK QUANTITY
        # ==================================

        try:
            quantity = int(
                input(
                    f"Enter quantity for "
                    f"{selected_item.name}: "
                )
            )

        except ValueError:
            print("\n❌ Invalid quantity!")
            print("Returning to the menu...")
            continue

        # Check quantity
        if quantity <= 0:

            print("\n❌ Quantity must be at least 1.")
            print("Returning to the menu...")
            continue

        # ==================================
        #        CALCULATE SUBTOTAL
        # ==================================

        subtotal = selected_item.get_price() * quantity

        # Add item to cart
        cart.append(
            (selected_item, quantity, subtotal)
        )

        print(
            f"\n✅ {quantity} x "
            f"{selected_item.name} added!"
        )

        print(f"Subtotal: ₱{subtotal:.2f}")

    return cart


# ==========================================
#            CALCULATE TOTAL
# ==========================================

def calculate_total(cart):

    total = 0

    for item, quantity, subtotal in cart:
        total += subtotal

    return total


# ==========================================
#             DISPLAY ORDER
# ==========================================

def display_order(cart):

    print("\n================================")
    print("          ORDER SUMMARY")
    print("================================")

    for item, quantity, subtotal in cart:

        print(f"{item.name}")

        print(
            f"  {quantity} x "
            f"₱{item.get_price():.2f}"
            f" = ₱{subtotal:.2f}"
        )

    print("--------------------------------")

    total = calculate_total(cart)

    print(f"TOTAL AMOUNT: ₱{total:.2f}")

    return total