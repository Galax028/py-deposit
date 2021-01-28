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

import random


low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
       'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
moderate = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
high = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '/', '{', '}', '[', ']', '+', '=', '<', '>', ':', ';']


def generatePassword():
    while True:
        chars = int(input("\tPlease specify the length for your password (Min: 4, Max: 32): "))
        if chars < 4 and chars != 0:
            print("\tError: The minimum length for generating a password is 4.\n")
        if chars <= 32 and chars >= 4:
            while True:
                password = []
                print("\n\n\tHow strong do you want you password to be?\n"
                      "\t\t1. Low (Lowercase and uppercase)\n"
                      "\t\t2. Moderate (Lowercase, uppercase and numbers)\n"
                      "\t\t3. High (Lowercase, uppercase, numbers and special characters)\n")
                prompt = int(input("py-deposit.passwordGenerator> "))
                if prompt == 1:
                    password += random.sample(low, chars)
                    print(f"\tYour password is: {''.join(password)}\n")
                    return ''.join(password)
                if prompt == 2:
                    password += random.sample(moderate, chars)
                    print(f"\tYour password is: {''.join(password)}\n")
                    return ''.join(password)
                if prompt == 3:
                    password += random.sample(high, chars)
                    print(f"\tYour password is: {''.join(password)}\n")
                    return ''.join(password)
                else:
                    print("\tError: Invalid argument.\n")
        if chars > 32:
            print("\tError: The maximum length for generating a password is 32.\n")
