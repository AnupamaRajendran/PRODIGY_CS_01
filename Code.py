def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice in ['E', 'D']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'E':
                print("Encrypted message:", encrypt(message, shift))
            else:
                print("Decrypted message:", decrypt(message, shift))
        else:
            print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
        
        continue_choice = input("Do you want to continue? (yes/no): ").lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()
