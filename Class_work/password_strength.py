#Surabya Satyal Password Strength Checker

points = 0
print("Welcome to the password checker.")
password = input("Write your password here: ") 
while password == "":
    password = input("That was not a valid input. Try again: ")

character = list(password) 
if any(char.islower() for char in character):
    points += 1

if any(char.isdigit() for char in character):
    points += 1

if any(char.isupper() for char in character):
    points += 1

if len(password) >= 8:
    points += 1

special_characters = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','[',']','{','}','|',';',':',',','.','<','>','?']

if any(char in special_characters for char in character):
    points += 1

if points <= 2:
    print("Your password is weak.")
elif points <= 3:
    print("Your password is moderate.")
elif points <= 4:
    print("Your password is strong.")
elif points <= 5:
    print("Your password is very strong.")


print(f"You got {points} out of 5")

    


