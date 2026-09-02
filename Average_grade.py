#Surabya Satyal Average Grade
print("Hello, today we are going to check your average grade.")

gradeA = float(input("Write your first grade!"))
gradeB = float(input("Write your second grade!"))
gradeC = float(input("Write your third grade!"))
gradeD = float(input("Write your forth grade!"))
gradeE = float(input("Write your fifth grade!"))
gradeF = float(input("Write your sixth grade!"))
gradeG = float(input("Write your seventh grade!"))

Avg = float(gradeA) + float(gradeB) + float(gradeC) + float(gradeD) + float(gradeE) + float(gradeF) + float(gradeG)
AvgFr = (Avg/7)
print("Your average grade is:", round(AvgFr,2))
