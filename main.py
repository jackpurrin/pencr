from cryptography.fernet import Fernet
from os import system, name
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys


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
    return open(keyName + ".key", "rb").read()
    print("Done!")
    menu()

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
    if task == "2" :
        print(load_key())
    if task == "3" :
        encrypt(input("What file do you want to encrypt? "), input("What is the name of the key to encrypt the file? "))
    if task == "4" :
        decrypt(input("What file do you want to decrypt? "), input("What is the key used to encrypt the file? "))

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    button1 = QPushButton(widget)
    button1.setText("Create Key")
    button1.move(0,0)
    button1.clicked.connect(button1_clicked)

    button2 = QPushButton(widget)
    button2.setText("Load Key")
    button2.move(0,32)
    button2.clicked.connect(button2_clicked)

    button3 = QPushButton(widget)
    button3.setText("Encrypt File")
    button3.move(0,64)
    button3.clicked.connect(button3_clicked)

    button4 = QPushButton(widget)
    button4.setText("Decrypt File")
    button4.move(0,96)
    button4.clicked.connect(button4_clicked)

    button5 = QPushButton(widget)
    button5.setText("Exit")
    button5.move(0,128)
    button5.clicked.connect(button5_clicked)

    widget.setGeometry(50,50,320,200)
    widget.setWindowTitle("Python Password Manager")
    widget.show()
    sys.exit(app.exec_())

def button1_clicked():
    write_key()

def button2_clicked():
    load_key()

def button3_clicked():
    encrypt(input("What file do you want to encrypt? "), input("What is the name of the key to encrypt the file? "))

def button4_clicked():
    decrypt(input("What file do you want to decrypt? "), input("What is the key used to encrypt the file? "))

def button5_clicked():
    exit()

if __name__ == '__main__':
   window()