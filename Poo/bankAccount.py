class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")
    
    def withdraw(self,amount):
        if self.is_active:
            if amount<= self.balance:
                self.balance-= amount
                print(f"Se ha retirado {amount}. Saldo actual es {self.balance}")

    def desactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido activada")

account1 = BankAccount("Ana",500)
account1 = BankAccount("Carlos", 1000)

#llamada a los metodos
account1.deposit(200)
account1.deposit(1000)
account1.desactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)
account1.withdraw(2250)