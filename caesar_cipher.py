# SCT_CYB_1 - Caesar Cipher Encryptor/Decryptor
# Author: Shivam Raj

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Encryptor / Decryptor ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted}")
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted}")
    else:
        print("Invalid choice. Please select 'e' or 'd'.")

if __name__ == "__main__":
    main()
