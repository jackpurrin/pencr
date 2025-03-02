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
    key_name = input("What do you want to name the key? ")
    
    key = Fernet.generate_key()
    with open(key_name + ".key", "wb") as key_file:
        key_file.write(key)

def load_key():
    clear()
    key_name = input("What is the key's name? ")
    
    print(open(key_name + ".key", "rb").read())
    input("Press anything to continue...")

def encrypt():
    clear()
    file_name = input("What file do you want to encrypt? ")
    key_name = input("What is the name of the key to encrypt the file? ")
    
    with open(file_name, "rb") as input_file:
        file_data = input_file.read()
    with open(key_name, "r") as key_file:
        key = key_file.read()
        
    f = Fernet(key)
    encrypted_data = f.encrypt(file_data)
    
    with open(file_name, "wb") as output_file:
        output_file.write(encrypted_data)

def decrypt():
    clear()
    file_name = input("What file do you want to decrypt? ")
    key_name = input("What is the key used to encrypt the file? ")
    
    with open(file_name, "rb") as input_file:
        file_data = input_file.read()
    with open(key_name, "r") as key_file:
        key = key_file.read()
        
    f = Fernet(key)
    decrypted_data = f.decrypt(file_data)
    
    with open(file_name, "wb") as output_file:
        output_file.write(decrypted_data)

def main():
    while True:
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
            encrypt()
        elif task == "4" :
            decrypt()
        else:
            break

if __name__ == "__main__":
    main()