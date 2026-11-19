#Surabya Satyal Order Up Period-1

total = 0
print("Welcome to the McDonald, where everything is higher price for lower quality.")

menu = {
    "Main": {
        "Big Mac": 6,
        "Cheeseburger": 3,
        "Hamburger": 4,
        "Filet-O-Fish": 5,
        "Mc Chicken": 3,
        "Chicken Mcnuggets(10)": 6,
    },
    "Side": {
        "Pizza McShaker Fries": 3,
        "McDonald's Fries": 3,
        "Apple Slices": 2,
        "Reindeer Treats": 2,
    },
        
    "Drink":{
        "Water": 2,
        "Coke": 3,
        "Vanilla Milkshake": 4,
        "Strawberry Milkshake": 4,
    } 
        
}

#Menu Display
print("The main menu options are:")
print(*menu["Main"])
print("The sides options are:")
print(*menu["Side"])
print("The drinks options are:")
print(*menu["Drink"])


def get_order(question, type):
   while True:
        food_option = input(question).title().strip()
        if food_option in menu[type]:
            return food_option
        print("This is a McDonald's Sir. We dont got that. PS.The ice-cream machine is broken. Spell corrctly!")
   
main_choice = get_order("What main course do you want(Just pick one): ", "Main")
first_side_choice = get_order("What first side do you want(Just pick one): ", "Side")
second_side_choice = get_order("What second side do you want(Just pick one): ", "Side")
drink_choice = get_order("What drink do you want(Just pick one): ", "Drink")
    

price_main = menu["Main"][main_choice]
price_side_one = menu["Side"][first_side_choice]
price_side_two = menu["Side"][second_side_choice]
drink_price = menu["Drink"][drink_choice]

reciept = price_main + price_side_one + price_side_two + drink_price

print("Your order was:")
print(f"Main Dish: {main_choice}")
print(f"Side Dishes: {first_side_choice} and {second_side_choice}")
print(f"Drink: {drink_choice}")
print(f"Total: ${reciept}")

while True:
    tip = input("Please give us the tip: ")
    if tip <= 0:
        print("What the heck")
    elif tip > 0:
        print("Thank you for helping the poor.")
    elif tip > 100:
        print("You the Mr. Beast.")
    else:
        break
    












