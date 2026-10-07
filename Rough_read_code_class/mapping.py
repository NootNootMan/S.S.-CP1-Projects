#SS Mapping Notes
def times(number): #Mapping
    return number*2

numbers = range(1,6)

multiplied_numbers = map(times, numbers) #Time is a function. Numbers in a list.

print(*list(multiplied_numbers)) #For loop
new_numbers = []
for number in numbers:
    new_numbers.append(number*2)

print(*new_numbers)