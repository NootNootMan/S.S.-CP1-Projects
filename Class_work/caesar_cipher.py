#Surabya Satyal Caesar Cipher Period-1

def cipher(message, shift_value, option): 
    if option == 'decode':
        shift_value = -shift_value

    result = []
    for char in message:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            new_char = chr((ord(char) - start + shift_value) % 26 + start)
            result.append(new_char)
        else:
            result.append(char)

    return "".join(result)

def question():
    choice = input("Type 1 to encode or type 2 to decode: ")
    if choice not in ['1', '2']:
        print("Use either 1 or 2")
        return

    actual_message = input("Enter the code: ")
    
    try:
        shift_value = int(input("By how much do you want to shift: "))
    except ValueError:
        print("Choose a number.")
        return
    
    
    option = 'encode' if choice == '1' else 'decode'
    processed_message = cipher(actual_message, shift_value, option)
    
    print(f"{option.capitalize()}d message: {processed_message}")

question()

