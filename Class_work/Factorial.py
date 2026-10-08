# Surabya Satyal Factorial Period-1
import math
numbers = []
factor_number = []
while True:
    user_input = input("What number do you want the factorial of: ")
    try:
        factor_user = int(user_input)
    except:
        print("That is not a number.")
    else:
        if 0 <= factor_user:
            break
        else:
            print("Thats a negetive number.")
numbers.append(factor_user)
factor_number.append(list(map(math.factorial,numbers)))
print(*factor_number)