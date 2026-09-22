#Surabya Satyal Crew shares
import random

while True:
    try:
        pirate_number = input("How many pirates do you have, including Quill and Yondo?")
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

money_units = treasure_got -int(pirate_number)*3
print("As Yondo and Quill gave 3 units to each member, there total treasure is now"+str(money_units)+".")
