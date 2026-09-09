#Surabya Satyal Idiot proof
while True:
    try:
        first_name = input("What is your first name: ").strip().title()#First name
        if not first_name.isalpha():
            print("Please enter a valid name.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid word for first name.")

while True:
    try:
        last_name = input("What is your last name: ").strip().title()#Last name
        if not last_name.isalpha():
            print("Name cannot be numbers. Please enter a valid name.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid word for last name.")

while True:
    try:
        phone_number = (input("What is phone number?: ").strip())#Phone number
        if not phone_number.isnumeric():
            print("Phone number cannot be letters. Please enter a valid phone number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for phone number.")

while True:
    try:
        gpa = float(input("What is your GPA: "))
    except:
        print("Thats not a valid GPA, try again")
    else:
        break      
full_name = first_name.title() + " " + last_name.title()
string_phone = str(phone_number)
#PRINT
print(f"Name: {full_name}")
print(f"Phone: {string_phone[0: 3]} {string_phone[3: 6]} {string_phone[6: 10]}")
print(f"GPA: {round(gpa, 1)}")
