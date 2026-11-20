# SS Flexible calculator
import math

#Stupid proofing
def type_of_question(equation, *question_type):
    while True:
        choice_question = input(equation).strip().lower()
        if choice_question in question_type:
            return choice_question
        else:
            print("The input wasn't correct. Please spell correctly.")

def actual_number():
    print("Enter numbers (type 'done' when finished)")
    numbers = []
    while True:
        user_message = input("Type the number you want to calculate: ").strip().lower()
        if user_message == "done":
            break
        try:
            numbers.append(float(user_message))
        except ValueError:
            print("Invalid input")
        return numbers
    
def calculator(operation, *numbers):
    if operation == "average":
        return sum(numbers) / len(numbers)
    elif operation == "product":
        return math.prod(numbers)
    elif operation == "sum":
        return sum(numbers)
    elif operation == "min":
        return min(numbers)
    elif operation == "max":
        return max(numbers)
    
user_numbers = actual_number()
    
choice_question = type_of_question("Which operation would you like to perform?")

if len(user_numbers) == 0:
    print("You didnt enter any numbers.")

else:
    answer = calculator()



    



