'''
A beginner-friendly Python expense tracker that calculates 
remaining balances, validates user input, and helps track spending.
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
        input("What was the price of the item(s): $")
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
    print("You have no more money to spend.")
    print(f"You owe the bank ${remain_balance}.")
elif remain_balance == 0:
    print("Your remaining balance is $0.")
    print("Let's keep that money out the red zone.")
else:
    print(f"Your remaining balance is ${remain_balance}.")
