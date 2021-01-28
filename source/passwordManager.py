# pylint: disable=unused-wildcard-import

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

from fernet import Fernet

from passwordGenerator import *

path = pathlib.Path(__file__).parent.absolute()
path = f"{path}\data\py-deposit.db"
key = Fernet(os.environ["PYDEPOSIT_ENCRYPTION_KEY"].encode('utf-8'))
conn = sqlite3.connect(path)
db = sqlite3.Cursor(conn)


def view():
    '''view       Show all the username and passwords stored in py-deposit.'''
    db.execute('''SELECT * FROM accounts''')
    output = db.fetchall()
    for i in range(len(output)):
        print(f"{output[i][0]}:\nUsername: {key.decrypt(output[i][1].encode('utf-8')).decode('utf-8')} | Password: {key.decrypt(output[i][2].encode('utf-8')).decode('utf-8')}\n")

def create():
    '''create    Create a new profile for saving a username and a password.'''
    create_pw = str(input("Do you want to create a new password? (y/n): "))
    if create_pw == "y":
        print("Please specify the name of the profile and a username.")
        profile_name = str(input("\tProfile name: "))
        username = key.encrypt(str(input("\tUsername: ")))
        password = key.encrypt(str(generatePassword()))
        print("\tSaving information...")
        db.execute('''INSERT INTO accounts (profile_name, username, password)
                      VALUES (?, ?, ?)''', (profile_name, username.decode('utf-8'), password.decode('utf-8')))
        conn.commit()
        print("\tAccount saved successfully.")
    elif create_pw == "n":
        print("Please specify the name of the profile, a username, and a password.")
        profile_name = str(input("\tProfile name: "))
        username = key.encrypt(str(input("\tUsername: ")))
        password = key.encrypt(str(input("\tPassword: ")))
        print("\tSaving information...")
        db.execute('''INSERT INTO accounts (profile_name, username, password)
                      VALUES (?, ?, ?)''', (profile_name, username.decode('utf-8'), password.decode('utf-8')))
        conn.commit()
        print("\tAccount saved successfully.")
    else:
        print("Error: Invalid argument.")

def delete(profile):
    '''delete [profile]    Delete a profile.'''
    warning = str(input(f"Are you sure you want to delete the \"{profile}\" profile? (y/n): "))
    if warning == "y":
        db.execute('''DELETE FROM accounts WHERE profile_name=(?)''', (profile,))
        conn.commit()
    elif warning == "n":
        print("Profile deletion canceled.")
    else:
        print("Error: Invalid argument.")
