# Improvements to make for v2.0

## 1. Handle non-numeric input
### What happens if someone types hello instead of a number?
float() will raise a ValueError, and your program will stop. Think about how you could handle that situation gracefully.



## 2. Check your amount_tries and price_tries variables
### You initialize both variables and increment them, but you never actually use their values.
Ask yourself: What purpose do these variables serve right now? You could use them to limit the number of retries or remove them until you need them.



## 3. Think about the negative balance message
### If the starting balance is $50 and the purchase costs $60, your calculation produces -10.
Your message says the user owes the bank $-10. That wording is a little confusing because the dollar amount is already negative. Consider how you want to communicate an overspending situation.



## 4. Improve how you display money
### What happens if the result is 12.5 or 12.5678?
Money is usually displayed with two decimal places, such as $12.50 or $12.57. Look into Python's f-string number formatting when you're ready.
