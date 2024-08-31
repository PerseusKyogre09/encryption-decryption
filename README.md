# Basic Encryption and Decryption Program

![Cryptography](https://www.publicdomainpictures.net/pictures/320000/nahled/cryptography-concept.jpg)

> **Note:** This project was originally intended to be my class 11th Computer Science project but was replaced by another idea. I've decided to upload it to GitHub as a fun and educational tool.

## 📜 Description

This is a basic encryption and decryption program written in Python, using the `cryptography` library. It allows you to securely encrypt and decrypt files with a randomly generated password. The program uses the `Fernet` symmetric encryption system to ensure your data is protected.

## 🛠 Features

- **File Encryption:** Select any file to encrypt using a randomly generated key.
- **File Decryption:** Decrypt the file using the correct password.
- **Password Protection:** A simple, randomly chosen password must be provided to decrypt the file.

## 🖼️ Demo

### Encrypting a File
![Encrypting](https://www.publicdomainpictures.net/pictures/300000/nahled/encrypting-file.jpg)

### Decrypting a File
![Decrypting](https://www.publicdomainpictures.net/pictures/320000/nahled/decrypting-file.jpg)

## 🚀 How It Works

1. **Key Generation:**
    - A symmetric encryption key is generated using `Fernet.generate_key()` and saved to a file (`key.key`).

2. **File Encryption:**
    - Select a file to encrypt via a file dialog.
    - The file is encrypted and saved as `output_file.txt` in the same directory.

3. **Password Generation:**
    - A simple password is randomly selected from a predefined list.

4. **File Decryption:**
    - Enter the correct password to decrypt the file back to its original form.

## 📂 File Structure

