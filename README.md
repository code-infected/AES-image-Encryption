## AES-image-Encryption

This project provides a Python script for encrypting and decrypting image files using the `cryptography` library's Fernet symmetric encryption. The script allows users to securely encrypt images and later decrypt them using a generated key.

## Features

- Encrypt image files to prevent unauthorized access.
- Decrypt previously encrypted image files using the same key.
- Automatically saves the key to a file during encryption for later use.

## Prerequisites

- Python 3.x
- `cryptography` library

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/code-infected/AES-image-Encryption.git
    cd your-repo-name
    ```

2. **Install the Required Packages:**

    Install the `cryptography` library if you haven't already:

    ```sh
    pip install cryptography
    ```

## Usage

### Encrypt an Image

1. Run the script with the path to the image file and the path where you want to save the key file:

    ```sh
    python main.py /path/to/your/image.jpg /path/to/save/key.key
    ```

2. Choose the encryption operation by entering `1`.

    ```sh
    Choose an operation:
    1. Encrypt
    2. Decrypt
    Enter choice (1 or 2): 1
    ```

    The script will generate a key, save it to the specified key file, encrypt the image, and save the encrypted image with `_encrypted` appended to the original image name.

### Decrypt an Image

1. Run the script with the path to the encrypted image file and the path to the key file:

    ```sh
    python main.py /path/to/your/image_encrypted.jpg /path/to/save/key.key
    ```

2. Choose the decryption operation by entering `2`.

    ```sh
    Choose an operation:
    1. Encrypt
    2. Decrypt
    Enter choice (1 or 2): 2
    ```

    The script will load the key from the specified key file, decrypt the image, and save the decrypted image with `_decrypted` appended to the encrypted image name.

## Example

### Encrypting an Image

```sh
python main.py my_image.jpg my_key.key
```

Output:

```
Choose an operation:
1. Encrypt
2. Decrypt
Enter choice (1 or 2): 1
Key saved to 'my_key.key'.
Image encrypted successfully. Encrypted image saved as 'my_image_encrypted.jpg'.
```

### Decrypting an Image

```sh
python main.py my_image_encrypted.jpg my_key.key
```

Output:

```
Choose an operation:
1. Encrypt
2. Decrypt
Enter choice (1 or 2): 2
Image decrypted successfully. Decrypted image saved as 'my_image_encrypted_decrypted.jpg'.
```

## Notes

- Keep the key file safe. Without it, you won't be able to decrypt the encrypted images.
- Ensure the paths to the image and key files are correct when running the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- Coded by [@Code-Infected](https://github.com/code-infected)

Feel free to open issues or pull requests if you find any bugs or have suggestions for improvements.
