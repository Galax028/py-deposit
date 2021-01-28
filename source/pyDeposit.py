# pylint: disable=import-error, undefined-variable, unused-wildcard-import

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
import sys

from authentication import *
from passwordGenerator import *
from passwordManager import *


__version__ = "1.0.0"
pathh = pathlib.Path(__file__).parent.absolute()
lic_path = str(pathh)[:-7]

def logo():
    print(" -----------------------------------------------------------------------------------------------------\n"
          "  \\\     ______   _   _         ______    ______   ______    ____     ______   _____   _______     //\n"
          "   \\\   |  __  | | | | |       |   _  \  |  ____| |  __  |  / __ \   / ____/  |_   _| |__   __|   //\n"
          "    \\\  | |__| | | |_| |  ___  |  | |  | | |____  | |__| | | |  | | | |____     | |      | |     //\n"
          "     || |  ____/  \   /  /__/  |  | |  | |  ____| |  ____/ | |  | |  \____ \    | |      | |    ||\n"
          "    //  | |        | |         |  |_|  | | |____  | |      | |__| |   ____| |  _| |_     | |     \\\ \n"
          "   //   |_|        |_|         |______/  |______| |_|       \____/   /_____/  |_____|    |_|      \\\ \n"
          "  //   -----------------------------------------------------------------------------------------   \\\ \n"
          "              http://www.apache.org/licenses/LICENSE-2.0 Copyright (c) 2020-2021 Galax028\n"
          " -----------------------------------------------------------------------------------------------------\n")

def _help(command):
    '''help <command>    Show help for py-deposit.'''
    if command == "create":
        print(create.__doc__)
    elif command == "delete":
        print(delete.__doc__)
    elif command == "help":
        print(_help.__doc__)
    elif command == "license":
        print(_license.__doc__)
    elif command == "quit":
        print(_quit.__doc__)
    elif command == "view":
        print(view.__doc__)
    else:
        with open(f"{pathh}\\data\\HELP.txt", "r") as f:
            print(f.read())
    print()

def _license():
    '''license    Show license for py-deposit.'''
    with open(f"{lic_path}\\LICENSE", "r") as f:
        print(f.read())
    print()

def _quit(exit_code=0):
    '''quit    Quit py-deposit.'''
    print("Exiting py-deposit...")
    sys.exit(exit_code)

def startupPrompt():
    print("Please login or register in order to use py-deposit.\n"
          "Type '1' to register.\n"
          "Type '2' to log in.\n"
          "Type '0' to quit.")

def mainHeader():
    logo()
    print(f"\nGalax028's py-deposit [version.{__version__}]\n"
           "(c) 2020 - 2021 Galax028. Some rights reserved.\n"
           "Type \"help\" for usage information. Type \"license\" to view the license.\n")

def main():
    loggedin = False
    while loggedin == False:
        startupPrompt()
        prompt = int(input("py-deposit.authentication> "))
        if prompt == 1:
            register()
            continue
        if prompt == 2:
            if login() == True:
                loggedin = True
                break
        if prompt == 0:
            print("Exiting py-deposit...")
            sys.exit(0)
        else:
            print("Invalid argument.\n")

    mainHeader()
    while loggedin == True:
        prompt = str(input("py-deposit> "))
        if prompt == "create":
            create()
            continue
        elif prompt == "delete":
            delete()
            continue
        elif prompt.startswith("help"):
            prompt = prompt[5:]
            _help(prompt)
            continue
        elif prompt == "license":
            _license()
            continue
        elif prompt == "quit":
            _quit()
        elif prompt == "view":
            view()
            continue
        else:
            print("Error: Invalid command or argument. Type \"help\" for help.")
            continue


if __name__ == '__main__':
    main()
