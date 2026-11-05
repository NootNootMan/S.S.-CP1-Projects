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
        user_input = input("By how much do you want to shift: ")
        shift_value = int(user_input)
    except ValueError:
        print(f"Choose a number.")
        return
    
    if choice == '1':
        encoded = cipher(actual_message, shift_value, 'encode')
        print(f"Encoded message: {encoded}")
    else:
        decoded = cipher(actual_message, shift_value, 'decode')
        print(f"Decoded message: {decoded}")

question()
