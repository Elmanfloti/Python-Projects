import random
import json

class Password :
    def __init__(self):
        self.Paswords= {}
    
    def gen_pass(self):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

        password = ""
        for i in range(9):
            password += random.choice(characters)
        print(password)

    def pass_check(self):
        while True:
            user_pass = input(" enter your password :\n")

            if len(user_pass) < 8:
                print("The password is weak please enter a strong password\n")
                continue

            has_number = False
            for char in user_pass:
                if char.isdigit():
                    has_number = True

            if not has_number:
                print("The password needs to have numbers in it\n")
                continue

            symbols = "!@#$%^&*()_-+=?/"
            has_symbol = False
            for char in user_pass:
                if char in symbols:
                    has_symbol = True

            if not has_symbol:
                print("The password needs to have symbols in it\n")
                continue

            print("Strong password!")
            break

    def save(self):
        with open("passwords.json", "w") as file:
            json.dump(self.Paswords, file)

    def load(self):
        try:
            with open("passwords.json", "r") as file:
                self.Paswords = json.load(file)
        except FileNotFoundError:
                print("No saved passwords found, starting fresh!")

    def menu(self):
        while True:
            choice = input("What do you want to do?\n1. Generate a password\n2. Check password strength\n3. Save a password\n4. Exit\n")
        
            if choice == "1":
                self.gen_pass()

            elif choice == "2":
                self.pass_check()

            elif choice == "3":
                site = input("Which site is this password for? ")
                user_password = input("Enter the password that you want to save: ")
                self.Paswords[site] = user_password
                self.save()

            elif choice == "4":
                break

pasword = Password()

pasword.load()

pasword.menu()