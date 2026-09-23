# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? "))#Made it an integer

total = price * quantity

discounted_total = total - (total * 0.10)#Changed 2 to total

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name)#It was snackName. So I changed it to snack_name.
print("Price per snack: " + str(price) + " credits")
print(" Total before tax: " + str(total))# I changed from price to total.
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")#The bracket wasnt closed. So I closed it.   