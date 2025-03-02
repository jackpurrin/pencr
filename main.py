from cryptography.fernet import Fernet
from os import system, name

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def write_key():
    clear()
    keyName = input("What do you want to name the key? ")
    key = Fernet.generate_key()
    with open(keyName + ".key", "wb") as key_file:
        key_file.write(key)
    print("Done!")
    menu()

def load_key():
    clear()
    keyName = input("What is the key's name? ")
    print(open(keyName + ".key", "rb").read())
    input("Press anything to continue...")

def encrypt(filename, key):
    clear()
    file = open(key, "r")
    content = file.read()
    key = content
    file.close()
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print("Done!")
    menu()

def decrypt(filename, key):
    clear()
    file = open(key, "r")
    content = file.read()
    key = content
    file.close()
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def menu():
    clear()
    print("1). Generate a key") 
    print("2). Read a key")
    print("3). Encrypt a file")
    print("4). Decrypt a file.")
    print("5). Exit")
    task = input("What do you want to do? ")

    if task == "1" :
        write_key()
    elif task == "2" :
        load_key()
    elif task == "3" :
        encrypt(input("What file do you want to encrypt? "), input("What is the name of the key to encrypt the file? "))
    elif task == "4" :
        decrypt(input("What file do you want to decrypt? "), input("What is the key used to encrypt the file? "))

menu()