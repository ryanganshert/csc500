"""
Part 1:
Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user
to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. Display
each of these amounts and the total price.
"""

food_charges = []
food_charge = 0
while str(food_charge)[0].upper() != "Q":
    food_charge = input("How much was your meal? (Type 'q' to quit): ")
    try:
        food_charges.append(round(float(food_charge), 2))
    except:
        try:
            if str(food_charge)[0].upper() == "Q":
                break
            else:
                print("Please enter a valid cost for your meal.")
        except:
            print("Please enter a valid cost for your meal.")

for i in range(len(food_charges)):
    tax = round(food_charges[i] * 0.07, 2)
    tip = round(food_charges[i] * 0.18, 2)
    print(f"Charge {i + 1} | ${food_charges[i]:.2f}:")
    print(f"\tTax: ${tax:.2f}")
    print(f"\tTip: ${tip:.2f}")
    print(f"\tTotal: ${food_charges[i] + tax + tip:.2f}")
print("Have a great day!!  :-)")
