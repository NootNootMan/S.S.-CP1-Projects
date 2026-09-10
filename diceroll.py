import random
dice_number = input("Hello, Which  size of dice would you like to roll?(D4, D6, D8, D10, D12, D20)")

if dice_number == "D4":#For d4
    d4 = random.randint(1,4)                
    print(d4) 

if dice_number == "D6":#For d6
    d6 = random.randint(1,6)
    print(d6) 

if dice_number == "D8":#For d8
    d8 = random.randint(1,8)
    print(d8) 

if dice_number == "D10":#For d10
    d10 = random.randint(1,10)
    print(d10) 

if dice_number == "D12":#For d12
    d12 = random.randint(1,12)
    print(d12) 

if dice_number == "D20":#For d20
    d20 = random.randint(1,20)
    print(d20) 

if dice_number =="D67":
    print("Get out of my code. Go to school")