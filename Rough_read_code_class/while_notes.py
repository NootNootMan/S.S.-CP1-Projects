#SS While Notes

import random
import time

goose = random.randint(1,20)
duck = 1 #Start point

while goose > duck: #End point
    print("Duck...")
    time.sleep(0.1)
    duck += 1 #Incrimentor    Used to change the itertor
    if duck == 15:
        print("Game over")
        break
else:
    print("GOOSE")


count = 30

while count > 1:
    print(count)
    time.sleep(.1)
    count -= 1


number = random.randint(1,1001)

while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 1000: "))
            if guess < 0 or guess > 1000:
                print("Idiot")
                continue
            break
        except:
            print("That isn't a number.")
    if guess == number:
            print("Congrats $1000")
            break
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("How did blud get here?")