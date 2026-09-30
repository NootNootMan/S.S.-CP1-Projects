#SS Lists, Tuples and Sets

#Lists
siblings = ["Tung-Tung","God of tung","Tesla Model YZ"," Mega Charizard XYZ","Micheal Jackson","Pneumonoultramicroscopicsilicovolcaniosis","Covid-19","Chat-gpt",] #Bracket around items. Each item must be a proper data types.
print(f"My oldest sibling is {siblings[1]}")
print(*siblings) #* unpacks operators
print(f"My youngest sibling is {siblings[-1]}")
siblings.append("Surabya") #Adds to the end.
siblings.insert(3, "Glorious Gaming Model O 2 PRO 4K/8K Wireless Gaming Mouse") #Adds to the told interval.
siblings.extend(["Mac-9 and cheese","Chick-fila Vanilla Milkshake","YOUR mom"]) #Adds things to the list.
siblings.remove("Surabya") #Removes things from the list.
siblings.pop(0) #Rmoves based on index.
print(*siblings)

print("")
print("")
print("")

#Tuples
subjects = ("CP1","Math","Biology","Geography")
print(subjects[2])
print(*subjects)

#Sets
visited = {"Utah","California"," North-Calorina","Nepal","Kathmandu","North-Korea","Atlantis"}

print(*visited)
print(len(visited))
visited.add("OHIO")
visited.update({"New york","Japan","Montana","Arizona","Mars"})
visited.remove("Japan")
print(*visited)
