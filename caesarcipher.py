def encrypt_caesar_cipher(message, shift_value):
    encrypted_message = ""
    for symbol in message:
        if symbol.isalpha():
            shift_base = ord('A') if symbol.isupper() else ord('a')
            encrypted_symbol = chr((ord(symbol) - shift_base + shift_value) % 26 + shift_base)
            encrypted_message += encrypted_symbol
        else:
            encrypted_message += symbol
    return encrypted_message

def decrypt_caesar_cipher(message, shift_value):
    decrypted_message = ""
    for symbol in message:
        if symbol.isalpha():
            shift_base = ord('A') if symbol.isupper() else ord('a')
            decrypted_symbol = chr((ord(symbol) - shift_base - shift_value) % 26 + shift_base)
            decrypted_message += decrypted_symbol
        else:
            decrypted_message += symbol
    return decrypted_message

def get_validated_input(prompt, input_type=str, condition=lambda x: True):
    while True:
        try:
            user_input = input_type(input(prompt).strip())
            if condition(user_input):
                return user_input
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

def main():
    while True:
        user_choice = get_validated_input("Do you want to (E)ncrypt, (D)ecrypt or (Q)uit? ", str, lambda x: x.upper() in ['E', 'D', 'Q']).upper()
        if user_choice == 'Q':
            print("Goodbye!")
            break
        
        user_message = get_validated_input("Enter the text: ", str)
        shift_amount = get_validated_input("Enter the shift value: ", int)
        
        if user_choice == 'E':
            result_message = encrypt_caesar_cipher(user_message, shift_amount)
            print(f"Encrypted text: {result_message}")
        elif user_choice == 'D':
            result_message = decrypt_caesar_cipher(user_message, shift_amount)
            print(f"Decrypted text: {result_message}")

if __name__ == "__main__":
    main()

