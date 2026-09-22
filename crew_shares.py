#Surabya Satyal Crew shares
import random

while True:
    try:
        pirate_number = input("How many pirates do you have including Quill and Yondo?")
        if not pirate_number.isnumeric():
            print("Put a valid number")
            continue
        break
    except ValueError:
        print("Invalid input.")

        print("So, in total you have"+pirate_number+"pirates")

        print("Yondu Udonta and his crew arrive at the Iron Lotus after several weeks of plundering various places around the galaxy. The crew has been in space for nearly six months and they are ready for a night of celebration. Yondu doesn't want to divvy up the plunder just yet, so he gives each crew member other than himself and Peter Quill 3 units and sends them off to the Iron Lotus. After the crew has gone, he and Peter count what's left and decide how to split it up among the crew. Yondu takes 13% of the total. He then gives Peter 11% of what's left. The next morning, Yondu divides the remaining amount evenly among all of the crew, including Yondu and Quill. The crew does not know that Yondu and Quill have already taken a cut.")

treasure_got = random.randint(500,5000)
print("They have "+str(treasure_got)+" units from the treasure.")
pirates_away = (pirates_number) - 2
money_units = treasure_got -int(pirate_away)*3
print("As Yondo and Quill gave 3 units to each member, there total treasure is now "+str(money_units)+".")


thief_yondo = round(13/100 *(money_units),2)
print("Now as the team was gone for the night, Yondu came and took 13% of the treasure which was a whopping "+str(thief_yondo)+" Units.")

thief_quill = round(11/100 *(money_units - thief_yondo),2)
print("Now as the team was gone for the night, Quill also came and took 11% of the treasure which was a whopping "+str(thief_quill)+" Units.")

remaining_treasure = money_units - thief_yondo - thief_quill
print("The day of splitting has arrived!!!")
money_for_all = round(((remaining_treasure) / int(pirate_number)) , 2)

print("Everyone in the crew got "+(money_for_all)+" units.")

real_yondo = (money_for_all) + (thief_yondo)
print("Yondo got "+str(real_yondo)+ "units.")

real_quill = (money_for_all) + (thief_quill)
print("Quill got "+str(real_quill)+ "units.")
