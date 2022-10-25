import string
from random import randint

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from hashlib import sha256

def generate_password(length=8, numbers=True, simbols=True):

    alowed_chars = string.ascii_letters
    if numbers: alowed_chars += string.digits
    if simbols: alowed_chars += string.punctuation

    n = len(alowed_chars)

    while True:
        password_result = ''
        
        for i in range(length):
            password_result += alowed_chars[randint(0, n-1)]

        has_number = any([char in string.digits for char in password_result])
        has_simbol = any([char in string.punctuation for char in password_result])

        if has_number == numbers and has_simbol == simbols:
            break

    return password_result

def generate_hash_bytes(password = str):

    return sha256(password.encode('utf-8')).digest()

def save_hash_bytes(hash = bytes):

    with open('hash.sha256', 'wb') as f:
        f.write(hash)

def get_hash_bytes():

    try:
        with open('hash.sha256', 'rb') as f:
            return f.readline()
    except FileNotFoundError:
        return None

def get_key_by_password(password = str):
    password = password.encode()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

def get_password_list(masterkey = str):
    
    passwords = []

    with open('passwords.list', 'rb') as encryted_file:
        decrypted_content = Fernet(get_key_by_password(masterkey)).decrypt(encryted_file.read())

    for line in decrypted_content.split('\n'):
    
        concept = ' '.join(line.split(' ')[0:-1])
        password = line.split(' ')[-1]

        passwords.append([concept, password])

    return passwords

def update_password_list(masterkey = str, new_list = list):

    content = '\n'.join([' '.join(item[0], item[1])for item in new_list])
    encrypted_content = Fernet(get_key_by_password(masterkey)).encrypt(content)
    print(content)

    with open('passwords.list', 'wb') as f:
        f.write(encrypted_content)

if __name__ == '__main__':
    
    get_hash_bytes()