#SS Function Notes
name = input("TELL ME YOUR GAWDDANG NAME: ")


def birthday(name, age = 35): #Keyword to define. Birthday is name of function. name is a parameter.
    print("Happy birthday to you")#content of function
    print("Happy birthday to you") 
    print(f'Happy birthday {name}') 
    print(f"You is now {age} years old.") 

def stupid_proof(user_answer, correct):
    user_answer = user_answer.strip().title()
    if user_answer in correct:
        return user_answer
    else:
        return False
print("March")
birthday("Bob", 55) #Argument
print("Neptune")
birthday("Stupid", 67)
print("UNKNOWN")
birthday("You",22)
birthday(name)


while True:
    capital = input("What's the capital of Utah: ")
    if stupid_proof(capital, ["Salt Lake City", "SLC", "Salt Lake"]):
        break
    else:
        print("Try again")
