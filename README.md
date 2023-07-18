# Image Encryption using AES

Image Encryption using AES is a project that demonstrates how to encrypt and decrypt images using the AES (Advanced Encryption Standard) algorithm in Python.

## Features

- Encrypt image files using AES encryption.
- Decrypt AES-encrypted image files.
- Command-line interface (CLI) for easy interaction.
- Uses the `cryptography` library for AES encryption.

## Requirements

- Python 3.6+
- `cryptography` library

## Installation

1. Clone the repository:

```shell
git clone git@github.com:code-infected/AES-image-Encryption.git

```markdown
Change into the project directory:

```shell
cd image-encryption-aes
```

Install the required dependencies:

```shell
pip install -r requirements.txt
```

Usage

To encrypt an image:

```shell
python image_encryption.py encrypt path/to/image.jpg
```

To decrypt an encrypted image:

```shell
python image_encryption.py decrypt path/to/encrypted_image.jpg
```

Replace `path/to/image.jpg` with the path to the image file you want to encrypt, and `path/to/encrypted_image.jpg` with the path to the encrypted image file you want to decrypt.

The encrypted image will be saved as `<original_image_name>_encrypted.jpg`, and the decrypted image will be saved as `<encrypted_image_name>_decrypted.jpg`.

Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.
```

