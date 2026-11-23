import math

#Stupid proofing
def type_of_question(prompt, *question_types):
    while True:
        choice_question = input(prompt).strip().lower()
        if choice_question in question_types:
            return choice_question
        print("The input wasn't correct. Please spell correctly.")

def actual_number():
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
    
#For the operation
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

#More stupid proofing
if len(user_numbers) == 0:
    print("You didnt enter any numbers.")

else:

    choice_question = type_of_question(
        "Which operation would you like to perform? (average, product, sum, min, max): ",
        "average", "product", "sum", "min", "max"
    )
    
    answer = calculator(choice_question, *user_numbers)
    print(f"{choice_question}: {answer}")