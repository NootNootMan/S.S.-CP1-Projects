#Surabya Satyal, Letter Grade

grade = int(input("What is your grade percentage?"))

if grade >=94:
    print(f"Your grade is a {grade}% have an A")
elif grade <= 93.9 and grade >= 90:
    print(f"Your grade is a {grade}% have an A-")
elif grade <= 89.9 and grade >= 87:
    print(f"Your grade is a {grade}% have an B+")
elif grade <= 86.9 and grade >= 84:
    print(f"Your grade is a {grade}% have an A-")

