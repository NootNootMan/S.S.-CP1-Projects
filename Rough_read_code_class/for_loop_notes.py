#SS For Loop Notes

import time
#Iteration
siblings = ["Tung-Tung","God of tung","Tesla Model YZ"," Mega Charizard XYZ","Micheal Jackson","Pneumonoultramicroscopicsilicovolcaniosis","Covid-19","Chat-gpt",]

for sibling in siblings: #For is the keyword Iterantion variable is sibling just after sibling. End sibling is name of a list.
    print(f"Good Morning{siblings}!")


grades = [100, 87, 53, 45, 78, 72, 88, 3, 94]
average = 0

for grade in grades:
    average += grade
    print(f"{grade} was added.")

average = average/len(grades)
print(f"The averager grade is {average:.2f}")

for i in range(2, 21, 2):
    print(i)
    time.sleep(0.5)

for i in range(20, 0, -1):
    print(i)
    time.sleep(0.25)
    if i == 1:
        print("You shall get nuked.")
        break


   

