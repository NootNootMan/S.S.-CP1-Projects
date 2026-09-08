"""name1 = input("What is your first name: ").strip().title()
name2 = input("What is your last name: ").strip().title()
seprated1 = name1.split()
fixed = "".join(seprated1)
seprated2 = name2.split()
fixed1 = "".join(seprated2)
full_name = fixed.title()+ " "+fixed1.title()
print("Hello "+full_name)#Comment

print(full_name.isalpha())
print(full_name.isnumeric())
print(full_name.isupper())"""

letter = input("Give me a letter :")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter = chr(number_value)
print(f"Your letter was {letter},now it is  {new_letter}")



