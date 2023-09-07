# Password Generator

import random

print("Welcome to the Random Password Generator! ")

upper_Case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_Case = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
all = upper_Case + lower_Case + numbers

while 1:
    password_length = int((input("\nEnter your desired character length up to 16 : ")))
    if password_length > 16:
        print("ERROR: Please choose a number between 1-16 ")
    else:
        password_count = int(input("How many passwords do you want? "))
        for x in range(0, password_count):
            password = ""
            for x in range(0, password_length):
                pass_characters = random.choice(all)
                password = password + pass_characters
            print("Your Password IS: " + password)




