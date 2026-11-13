#Surabya Satyal Combat Pragram Period-1
import random

pirate_token = random.randint(1,15)
if pirate_token == random.randint(1,15):
    print("You got pirate token.")

defence = 0
health = 0
attack_bonus = 0
damage_bonus = 0

print("Wecome to the combat program.")
name = input("What is your name?")
print('(Some backstory) You are a hunter and you hunt creatures for a living.')
user_class = int(input("What class of fighter are you? 1 if you are a Fighter 2 if you are a Mage 3 if you are a Rogue."))

if user_class == 1:
    defence = 14
    health = 30
    attack_bonus = 3
    damage_bonus = 4

elif user_class == 2:
    defence = 9
    health = 25
    attack_bonus = 4
    damage_bonus = 5

elif user_class == 3:
    defence = 20
    health = 40
    attack_bonus = 2
    damage_bonus = 2

    
real_attack = random.randint(1,20) + attack_bonus
real_damage = random.randint(1,8) + damage_bonus

print("Your stats are:")
print(f"Defence = {defence}")
print(f"Health = {health}")
print(f"Damage = {real_damage}")
print(f"Attack = {real_attack}")
    
    
  

    





