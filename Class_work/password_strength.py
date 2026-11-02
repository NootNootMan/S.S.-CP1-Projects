#Surabya Satyal Password Strength Checker

points = 0
print("Welcome to the password checker.")
password = input("Write your password here: ") 
while password == "": #Idiot proofing
    password = input("That was not a valid input. Try again: ")

character = list(password) 
if any(char.islower() for char in character): # Checks if each character is lowercase
    points += 1

if any(char.isdigit() for char in character): # Checks if each character is a number
    points += 1

if any(char.isupper() for char in character): # Checks if each character is uppercase
    points += 1

if len(password) >= 8: # Checks if password is longer or equal to 8 characters
    points += 1

# Declares the list of possible characters that are categorized as special to be used in following code
special_characters = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','[',']','{','}','|',';',':',',','.','<','>','?']

# Checks if each character has a special character
if any(char in special_characters for char in character):
    points += 1

#Checks the points and give an output
if points <= 2:
    print("Your password is weak.")
elif points <= 3:
    print("Your password is moderate.")
elif points <= 4:
    print("Your password is strong.")
elif points <= 5:
    print("Your password is very strong.")

# Prints the points
print(f"You got {points} out of 5")

    


