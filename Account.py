class Account:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
        print("Welcome" , self.owner, "Your balance:", self.balance)
        
    def deposit(self,summa):
        self.balance+=summa
        print("Your balance now:", self.balance)
    def withdraw(self, withdrawsumm):
        if self.balance < withdrawsumm:
            print(self.owner, "you dont have enough money on you account! Replenish your balance!")
        else:
            self.balance -= withdrawsumm
            print("Succesfully! Your balance now:", self.balance)

account = Account("David", 0 )
account.deposit(50000)
account.withdraw(20000)