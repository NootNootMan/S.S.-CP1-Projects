# Surabya Satyal Factorial Period-1 
import math # Importing math
numbers = [] # Empty list

while True:
    user_input = input("What number do you want the factorial of: ")
    try:
        factor_user = int(user_input)
    except ValueError:
        print("That is not a number.")
    else:
        if factor_user >= 0:
            break
        else:
            print("That is a negative number.")

numbers.append(factor_user) # Store the user input.

factor_results = list(map(math.factorial, numbers))# Use map and then convert into list.

for i in range(len(numbers)): # Using index to print the correct output. 
    print(f"{numbers[i]}! = {factor_results[i]}")
