## AES-image-Encryption

This is a Python script that demonstrates image encryption and decryption using the AES (Advanced Encryption Standard) algorithm.

## Features

- Encrypt an image file using AES encryption.
- Decrypt an AES-encrypted image file.
- Command-line interface (CLI) for easy interaction.
- Uses the `cryptography` library for AES encryption.

## Requirements

- Python 3.6+
- `cryptography` library
- `argparse` library

## Usage

1. Clone the repository:

```shell
git clone https://github.com/code-infected/AES-image-Encryption.git
```

2. Change into the project directory:

```shell

cd AES-image-Encryption
```

2. Install the required dependencies:

```shell

pip install -r requirements.txt

```

3. Run the script with the image file path as a command-line argument:

```shell
python main.py path/to/image.jpg
```

Replace `path/to/image.jpg` with the actual path to the image file you want to encrypt or decrypt.

4. Choose the desired operation:
   - Enter `1` to encrypt the image.
   - Enter `2` to decrypt the image.

The encrypted image will be saved as `<original_image_name>_encrypted.jpg`, and the decrypted image will be saved as `<encrypted_image_name>_decrypted.jpg`.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

