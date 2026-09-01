# ==========================================
#        MANG INASAL ORDERING SYSTEM
# ==========================================

from ordering import take_order
from ordering import display_order
from ordering import calculate_total


print("================================")
print("      WELCOME TO MANG INASAL")
print("================================")


# ==========================================
#              TAKE ORDER
# ==========================================

cart = take_order()


# ==========================================
#            DISPLAY ORDER
# ==========================================

total = display_order(cart)


# ==========================================
#               PAYMENT
# ==========================================

while True:

    try:
        money = float(
            input("\nEnter amount of money: ₱")
        )

    except ValueError:
        print("\n❌ Invalid amount!")
        print("Please enter a valid number.")
        continue

    # Prevent negative money
    if money < 0:

        print("\n❌ Amount cannot be negative.")
        continue


    # ======================================
    #          NOT ENOUGH MONEY
    # ======================================

    if money < total:

        print("\n================================")
        print("         PAYMENT FAILED")
        print("================================")

        print(f"Total: ₱{total:.2f}")
        print(f"Your money: ₱{money:.2f}")
        print(
            f"Short by: "
            f"₱{total - money:.2f}"
        )

        print("\n❌ Insufficient money!")
        print("Your receipt will NOT be printed.")

        print("\nThank you for visiting Mang Inasal!")
        print("================================")

        break


    # ======================================
    #             ENOUGH MONEY
    # ======================================

    else:

        change = money - total

        print("\n================================")
        print("          MANG INASAL")
        print("            RECEIPT")
        print("================================")

        for item, quantity, subtotal in cart:

            print(f"{item.name}")

            print(
                f"  {quantity} x "
                f"₱{item.get_price():.2f}"
                f" = ₱{subtotal:.2f}"
            )

        print("--------------------------------")
        print(f"TOTAL:  ₱{total:.2f}")
        print(f"CASH:   ₱{money:.2f}")
        print(f"CHANGE: ₱{change:.2f}")

        print("================================")
        print("     Thank you for ordering!")
        print("     Please come again!")
        print("================================")

        break