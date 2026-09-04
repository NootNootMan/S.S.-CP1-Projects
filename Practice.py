name1 = input("What is your first name: ").strip().title()
name2 = input("What is your last name: ").strip().title()
seprated1 = name1.split()
fixed = "".join(seprated1)
seprated2 = name2.split()
fixed1 = "".join(seprated2)
full_name = fixed.title()+ " "+fixed1.title()
print("Hello "+full_name)#Comment

print(full_name.isalpha())
print(full_name.isnumeric())
print(full_name.isupper())


