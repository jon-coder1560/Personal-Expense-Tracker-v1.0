'''
    Personal Expense Tracker v1.0
    1. Ask the user how much money they have.
    2. Ask for the price of an item they purchased.
    3. Calculate the remaining balance.
    4. Display the result clearly.
    5. Add checks for invalid input.
    6. Expand it to handle multiple purchases.
'''

def bank_total():
    total_amount = float(
        input("How much money do you have: $")
    )
    amount_tries = 0
    while total_amount < 0:
        print("Amount cannot be less than 0")
        total_amount = float(
            input("How much money do you have: $")
        )
        amount_tries += 1
    return total_amount

def item_total():
    item_price = float(
        input("\nWhat was the price of the item(s): $")
    )
    price_tries = 0
    while item_price < 0:
        print("Price cannot be less than 0.")
        item_price = float(
            input("What was the price of the item(s): $")
        )
        price_tries += 1
    return item_price

total_amount = bank_total()
item_price = item_total()

remain_balance = total_amount - item_price

if remain_balance < 0:
    print("\nYou have no more money to spend.")
    print(f"Your balance is ${remain_balance}.")
elif remain_balance == 0:
    print("\nYour remaining balance is $0.")
    print("Let's keep that money out the red zone.")
else:
    print(f"\nYour remaining balance is ${remain_balance}.")
