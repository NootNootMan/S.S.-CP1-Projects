#Surabya Satyal Escape room Period-1
code = ("Fortnitemashedpotato")
tries = 0

while True:
        guess = (input("Guess the code: "))
        if guess == code:
            print("Congrats,you escaped.")
            break
        if tries == 0:
                print("Incorrect! Hint: It's three words mixed into one word.")
                tries += 1
                print(f"You have used {tries} of your 3 tries. Be careful")
        elif tries == 1:
                print("Incorrect! Hint: It's a dead fps game and a food made using potatoes.")
                tries += 1
                print(f"You have used {tries} of your 3 tries. Be careful")
        elif tries == 2:
                print("Incorrect! Hint: It's a shooting game where you can build stuff and a food made from squising potatoes and it is all singular not plural.First letter is capital.")
                tries += 1
                print(f"You have used {tries} of your 3 tries. Be careful")
        else:
               print("You are out of tries. Now, you rot in the room forever.")
               break
        
        