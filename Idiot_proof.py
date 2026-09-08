while True:
    try:
        first_name = input("What is your first name: ").strip().title()
        if not first_name.isalpha():
            print("Please enter a valid name.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid word for first name.")

while True:
    try:
        last_name = input("What is your last name: ").strip().title()
        if not last_name.isalpha():
            print("Name cannot be numbers. Please enter a valid name.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid word for last name.")

while True:
    try:
        phone_number = int.input("What is phone number?: ").strip()
        if not last_name.isnumeric():
            print("Phone number cannot be letters. Please enter a valid phone number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for phone number.")

while True:
    try:
        gpa = int.input("What is your GPA?: ").strip()
        if not gpa.replace('.', '', 1).isnumeric():
            print("GPA cannot be letters. Please enter a valid GPA.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for GPA.")        

        print(f"Name: {first_name+last_name}")
        print(f"Phone: {phone_number}")
        print(f"GPA:{gpa}")
