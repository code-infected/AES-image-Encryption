import argparse
from cryptography.fernet import Fernet


def encrypt_image(image_path, key):
    with open(image_path, 'rb') as file:
        original_data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(original_data)

    encrypted_image_path = image_path[:-4] + '_encrypted.jpg'

    with open(encrypted_image_path, 'wb') as file:
        file.write(encrypted_data)

    print(f"Image encrypted successfully. Encrypted image saved as '{encrypted_image_path}'.")


def decrypt_image(encrypted_image_path, key):
    with open(encrypted_image_path, 'rb') as file:
        encrypted_data = file.read()

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    decrypted_image_path = encrypted_image_path[:-4] + '_decrypted.jpg'

    with open(decrypted_image_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"Image decrypted successfully. Decrypted image saved as '{decrypted_image_path}'.")


def main():
    parser = argparse.ArgumentParser(description='Image Encryption using AES')
    parser.add_argument('image_path', type=str, help='Path to the image file')
    args = parser.parse_args()

    # Generate AES key
    key = Fernet.generate_key()

    choice = input("Choose an operation:\n1. Encrypt\n2. Decrypt\nEnter choice (1 or 2): ")

    if choice == '1':
        encrypt_image(args.image_path, key)
    elif choice == '2':
        decrypt_image(args.image_path, key)
    else:
        print("Invalid choice. Please choose either 1 or 2.")


if __name__ == '__main__':
    main()
