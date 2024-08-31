import os
import time
import getpass
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from cryptography.fernet import Fernet

def encrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)


key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

Tk().withdraw()
input_file = askopenfilename(title="Select Input File")

if not input_file:
    print("File selection canceled.")
    exit()

input_directory = os.path.dirname(input_file)
output_file = os.path.join(input_directory, "output_file.txt")

encrypt_file(input_file, output_file, key)

select_pass = ['cat', 'penguin', 'computer', 'python', 'banana']

password = random.choice(select_pass)
print("Your password is:", password)
time.sleep(10)

clear_command = "cls" if os.name == "nt" else "clear"
os.system(clear_command)

user_password = getpass.getpass("Enter the password to decrypt the file: ")

if user_password == password:
    decrypt_file(output_file, input_file, key)
    print("File decrypted successfully.")
else:
    print("Incorrect password. File cannot be decrypted.")
