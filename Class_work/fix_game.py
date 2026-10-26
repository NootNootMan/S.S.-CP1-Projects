import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number: # Missing the : .Syntax error. Without the : nothing will happen if you guess or dont guess the code.
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print("Your guesses per round: ",scores) # Was concatinating a list. Syntax error. You cant concatinate a list so it doesnt show the guesses.

total = 0
for score in scores:
                            # Total = 0 was inside loop. Logic error. The loop resets the total to 0 every time.
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(average))

best_round = min(scores) # There was a -1. Logic error. There was a -1 before rounds making it ignore the last score.


print(f"Your best round took only {best_round} guesses!")
