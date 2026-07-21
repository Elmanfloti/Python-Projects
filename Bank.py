import json
class Bank :
    def __init__(self):

        self.bank_money= 0


    def save(self):

        data = {"bank_money": self.bank_money}
        with open("bank.json", "w") as file:

            json.dump(data, file)


    def open_ops(self):

        open_bank=input("Do you want to open a bank acount\n").lower()
        if open_bank =="yes":

            options=input("what do you want:\n1_ adding money into an account\n2_taking money out of an account\n3_moving money from one account to another\n4_Check balance\n")

            if options == "1":

                add=int(input("who much money you want to add: "))
                self.bank_money += add
                self.save()
             

            if options =="2":

                take=int(input("who much money you want to take: "))

                if self.bank_money >= take :

                    self.bank_money -= take

                else :

                    print(f"sorry but you dont have {take} in your bank acount")

                self.save()


            if options=="3":

                transfer=int(input("who much money you want to transfer: "))

                if self.bank_money >= transfer :
                    
                    self.bank_money -= transfer
                    print(f"You transferred {transfer} dollars.")

                else :

                    print(f"sorry but you dont have {transfer} in your bank acount")

                self.save()

            if options == "4":

                print(f"Your current balance is {self.bank_money} dollars.")
                self.save()
    
    def load(self):

        try:
            with open("bank.json", "r") as file:
                data = json.load(file)
            self.bank_money = data["bank_money"]

        except FileNotFoundError:
            print("No saved bank data found, starting fresh!")


bank=Bank()

bank.load()

bank.open_ops()


                


 
