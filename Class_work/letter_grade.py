#Surabya Satyal, Letter Grade

grade = float(input("What is your grade percentage?"))

   
if grade >=94:
    print(f"Your grade is a {grade}% have an A")
elif grade <= 93.9 and grade >= 90:
    print(f"Your grade is a {grade}% have an A-")
elif grade <= 89.9 and grade >= 87:
    print(f"Your grade is a {grade}% have an B+")
elif grade <= 86.9 and grade >= 84:
    print(f"Your grade is a {grade}% have an B")
elif grade <= 83.9 and grade >= 80:
    print(f"Your grade is a {grade}% have an B-")
elif grade <= 79.9 and grade >= 77:
    print(f"Your grade is a {grade}% have an C+")  
elif grade <= 76.9 and grade >= 74:
    print(f"Your grade is a {grade}% have an C")  
elif grade <= 73.9 and grade >= 70:
    print(f"Your grade is a {grade}% have an C-")
elif grade <= 69.9 and grade >= 67:
    print(f"Your grade is a {grade}% have an D+")
elif grade <= 66.9 and grade >= 64:
    print(f"Your grade is a {grade}% have an D")
elif grade <= 63.9 and grade >= 60:
    print(f"Your grade is a {grade}% have an D-")
elif grade <0:
    print(f"Please put a valid number.")
else:
    print(f"Your grade is a {grade}% have an F")


    



