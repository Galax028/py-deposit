# pylint: disable=anomalous-backslash-in-string

# -----------------------------------------------------------------------------------------------------
#  \\     ______   _   _         ______    ______   ______    ____     ______   _____   _______     //
#   \\   |  __  | | | | |       |   _  \  |  ____| |  __  |  / __ \   / ____/  |_   _| |__   __|   //
#    \\  | |__| | | |_| |  ___  |  | |  | | |____  | |__| | | |  | | | |____     | |      | |     //
#     || |  ____/  \   /  /__/  |  | |  | |  ____| |  ____/ | |  | |  \____ \    | |      | |    ||
#    //  | |        | |         |  |_|  | | |____  | |      | |__| |   ____| |  _| |_     | |     \\
#   //   |_|        |_|         |______/  |______| |_|       \____/   /_____/  |_____|    |_|      \\
#  //   -----------------------------------------------------------------------------------------   \\
#              http://www.apache.org/licenses/LICENSE-2.0 Copyright (c) 2020-2021 Galax028
# -----------------------------------------------------------------------------------------------------

import os
import pathlib
import sqlite3
import subprocess
import sys

from fernet import Fernet

path = pathlib.Path(__file__).parent.absolute()
path = f"{path}\data\py-deposit.db"
conn = sqlite3.connect(path)
db = sqlite3.Cursor(conn)


def register():
    db.execute('''CREATE TABLE IF NOT EXISTS info (
                  username TINYTEXT NOT NULL,
                  password TINYTEXT NOT NULL)''')
    db.execute("SELECT EXISTS(SELECT 1 FROM info)")
    registerCheck = db.fetchone()
    if registerCheck == (1,):
        print("Error: A py-deposit account already exists. Please log in.\n")
        return
    while True:
        print("Register for py-deposit:")
        print("\n\tStep 1: Fill in your information")
        username = str(input("\t\tUsername: "))
        password = str(input("\t\tMaster Password: "))
        passwordCheck = str(input("\t\tConfirm Master Password: "))
        if password != passwordCheck:
            print("\t\tError: Master password does not match. Please check for any mistakes.\n")
        else:
            print("\t\tGenerating encryption key...")
            key = Fernet.generate_key()
            encryptor = Fernet(key)
            subprocess.Popen(["setx", "PYDEPOSIT_ENCRYPTION_KEY", key.decode('utf-8')])
            print("\t\tCreating database table...")
            db.execute('''CREATE TABLE IF NOT EXISTS accounts (
                          profile_name TINYTEXT NOT NULL,
                          username TINYTEXT NOT NULL,
                          password TINYTEXT NOT NULL)''')
            print(f"\t\tHello and welcome to py-deposit, {username}!")
            username = encryptor.encrypt(username.encode('utf-8'))
            password = encryptor.encrypt(password.encode('utf-8'))
            db.execute('''INSERT INTO info (username, password)
                          VALUES (?, ?)''', (username.decode('utf-8'), password.decode('utf-8')))
            conn.commit()
            sys.exit(0)

def login():
    db.execute('''SELECT username FROM info''')
    usernameCheck = ''.join(db.fetchone()).encode('utf-8')
    db.execute('''SELECT password FROM info''')
    passwordCheck = ''.join(db.fetchone()).encode('utf-8')
    decryptor = Fernet(os.environ["PYDEPOSIT_ENCRYPTION_KEY"].encode('utf-8'))
    usernameCheck = decryptor.decrypt(usernameCheck).decode('utf-8')
    passwordCheck = decryptor.decrypt(passwordCheck).decode('utf-8')
    while True:
        print("Log in to py-deposit:")
        username = str(input("\tUsername: "))
        password = str(input("\tMaster Password: "))
        if (username == usernameCheck) and (password == passwordCheck):
            print("Login successful! Welcome to py-deposit.\n")
            return True
        else:
            print("Error: Incorrect username or password. Please try again.\n")
            continue
