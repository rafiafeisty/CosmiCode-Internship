class bank:
    def __init__(self,account_number,balance,owner_name):
        self.balance=balance
        self.account_number=account_number
        self.owner_name=owner_name
    def deposit(self):
        print("---------------------------")
        print("DEPOSIT MONEY")
        amount=int(input("Enter the amount: "))
        self.balance=self.balance+amount
        print("New Balance: ",self.balance)
    def withdraw(self):
        print("---------------------------")
        print("WITHDRAW MONEY")
        amount=int(input("Enter the amount: "))
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print("New Balance: ",self.balance)
    def tranfer(self,recepient_account):
        print("---------------------------")
        print("TRANSFER MONEY")
        if recepient_account.account_number==self.account_number:
            print("You can't transfer to your own account")
            return
        amount=int(input("Enter the amount: "))
        if amount>self.balance:
            print("Insufficent Balance")
            return
        else:
            self.balance=self.balance-amount
            recepient_account.balance+=amount
            print("Amount ", amount, " transfered from ",self.account_number, " Account to ",recepient_account.account_number, " Account")
            print("New Balance: ",self.balance)
    def details(self):
        print("---------------------------")
        print("Owner Name: ",self.owner_name)
        print("Account Number: ",self.account_number)
        print("Balance: ",self.balance)
        print("---------------------------")

b1=bank(1001,5000,"user1")
b2=bank(1003,5000,"user2")
b1.details()
print("\n")
b1.tranfer(b2)
b1.deposit()
b1.withdraw()
print("\n")
b1.details()