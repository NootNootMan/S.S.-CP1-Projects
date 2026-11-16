#Surabya Satyal Combat Pragram Period-1
import random

import random

pirate_token = random.randint(1, 15)
if pirate_token == random.randint(1, 15):
    print("You got pirate token.")

defence = 0
health = 0
attack_bonus = 0
damage_bonus = 0

print("Welcome to the combat program.")
name = input("What is your name? ")
print("(Some backstory) You are a hunter and you hunt creatures for a living.")

while True:
    user_class = input("What class are you? 1:Fighter, 2:Mage, 3:Rogue: ")

    if user_class == "1":
        defence = 14
        health = 30
        attack_bonus = 3
        damage_bonus = 4
        break
    elif user_class == "2":
        defence = 10
        health = 27
        attack_bonus = 6
        damage_bonus = 6
        break
    elif user_class == "3":
        defence = 15
        health = 50
        attack_bonus = 2
        damage_bonus = 2
        break
    else:
        print("You can only pick 1, 2, or 3.")

real_attack = random.randint(1, 20) + attack_bonus
real_damage = random.randint(1, 8) + damage_bonus

print("Your stats are:")
print(f"Defence = {defence}")
print(f"Health = {health}")
print(f"Damage = {real_damage}")
print(f"Attack = {real_attack}")

print("You are walking down a forest and suddenly a bear approaches you!")

bear_type = "Crystal"
bear_defence = 13
bear_health = 40
bear_damage = 12
bear_attack = 15

print(f"{bear_type} Bear stats are:")
print(f"Defence = {bear_defence}")
print(f"Health = {bear_health}")
print(f"Damage = {bear_damage}")
print(f"Attack = {bear_attack}")

turn = random.randint(1, 2)
if turn == 1:
    print("You get the first move!")
else:
    print("The bear gets the first move!")

while health > 0 and bear_health > 0:

    if turn == 1:
        print("What would you like to do?")
        form_attack = input("1: Normal attack | 2: Wild attack | 3: Heal potion | 4: Flee: ")

        if form_attack == "1":
            if real_attack >= bear_defence:
                bear_health -= real_damage
                print(f"You hit the bear for {real_damage} damage!")
            else:
                print(f"Your attack of {real_attack} missed the bear's defence of {bear_defence}!")
            print(f"Your health: {health} and Bear health: {bear_health}")

        elif form_attack == "2":
            wild_attack = real_attack - 3
            health -= 3
            wild_damage = real_damage + 5
            if wild_attack >= bear_defence:
                bear_health -= wild_damage
                print(f"Wild hit! You dealt {wild_damage} damage!")
            else:
                print(f"Your wild attack of {wild_attack} missed!")
            print(f"Your health: {health} and Bear health: {bear_health}")

        elif form_attack == "3":
            heal = random.randint(6, 10)
            health += heal
            print(f"You used a heal potion and gained {heal} health.")
            print(f"Your health: {health} and Bear health: {bear_health}")

        elif form_attack == "4":
            chance_flee = random.randint(1, 2)
            if chance_flee == 1:
                print("You fled the battle!")
                break
            elif chance_flee == 2:
                print("Bear didnt let you escape. LOL")

        else:
            print("Thats not a choice. Your turn is gone.")

        turn = 2

    elif turn == 2:
        print(f"The {bear_type} Bear attacks you.")
        if bear_attack >= defence:
            health -= bear_damage
            print(f"The bear hits you for {bear_damage} damage!")
        else:
            print("You blocked the bear's attack!")
        print(f"Your health: {health} and Bear health: {bear_health}")

        turn = 1

if health <= 0:
    print("You died. Better luck next time.")
elif bear_health <= 0:
    print("Nice one. The bear died and you survive.")
