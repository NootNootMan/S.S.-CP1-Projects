#SS Elif and Logical Operator Notes

age = 18 # The age
licence = False #See if you got a licence

if age >= 18:
    print('You are an adult, hopefully you have a job unc.')
elif age >= 15 and licence: #And is true
    print("You can drive but you still need to go to the school LOL")
elif age >= 15 and not licence: #And not is false
    print("You cant drive so, you need to walk to school.")
else:
    print('Hello my child, I am you long lost dad. Now get back to work at school.')    


win = True
hp = 25


if win or hp < 1:
    print("Game Over LOSER!")
    if hp > 0:
        pass
    else:
        print("You LOST.")

else:
    print("The game is still going. LOCK IN")