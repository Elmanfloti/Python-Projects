class Transaction:
    def __init__(self,catagory, amount, type):
        self.catagory=catagory
        self.amount=amount
        self.type=type

    def datetime(self):
        import datetime
        now = datetime.datetime.now()
        print(now)

    def status(self):
        print(f" {self.type} - {self.catagory} : {self.amount}DA ")
    
transaction= Transaction("food", 500, "Expense")
transaction.datetime()
transaction.status()
