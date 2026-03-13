class BankAccount:
    bank_name = 'Azure Bank'
    def __init__(self,owner,balance,acctype):
        self.owner = owner
        self.balance = balance
        self.acctype = acctype
        print('=' * 45)
        print(f"Welcome to {self.bank_name} - {self.owner} and Your Balance is {self.balance}")
        print(f"Owner : {self.owner}")
        print(f"Balance {self.balance}")
        print(f"Account Type : {self.acctype}")
        print('=' * 45)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value < 0:
            print("Balance cannot be zero")
            self._balance = 0
        elif value > 1000000:
            print(f"Balance exceeds Limit")
            self._balance = 1000000
        else:
            self._balance = value

    def deposit(self,amount):
        self.balance += amount
        print('=' * 45)
        print(f"Money Deposited : {amount} and Your Current Balance : {self.balance}")
        print('=' * 45)

    def withdraw(self,amount):
        if amount > self.balance:
            print('=' * 45)
            print(f"Insufficient Balance Your Current Balance : {self.balance}")
            print('=' * 45)
        else:
            self.balance -= amount
            print('=' * 45)
            print(f"Money withdrawn : {amount} and Your Current Balance : {self.balance}")
            print('=' * 45)

    def get_summary(self):
        print('=' * 45)
        print(f"Owner : {self.owner} | Balance : {self.balance}")
        print('=' * 45)

class HDFCAccount(BankAccount):
    def __init__(self,owner,balance,acctype):
        super().__init__(owner,balance,acctype)
        self.transaction_fee = 0.05

    def withdraw(self,amount):
        fee = round(amount* self.transaction_fee,2)
        total = amount + fee
        if total > self.balance:
            print('=' * 45)
            print(f"Insufficient Funds")
            print('=' * 45)
        else:
            print('=' * 45)
            print(f"Withdrawn Rs.{amount} "
                       f"+ fee Rs.{fee} |"
                       f"Balance : Rs.{self.balance}")
            print('=' * 45)

class ICICIAccount(BankAccount):
    def __init__(self,owner,balance,acctype):
        super().__init__(owner,balance,acctype)
        self.interest_rate = 0.05

    def add_interest(self):
        interest = round(self.balance * self.interest_rate,2)
        self.balance += interest
        print('=' * 45)
        print(f"Interest : {interest} added")
        print('=' * 45)

class LICBank(BankAccount):
    def __init__(self,owner,balance,acctype,policy_number):
        super().__init__(owner,balance,acctype)
        self.policy_number = policy_number

    def get_summary(self):
        print('=' * 45)
        print(f" Account Summary")
        print('=' * 45)
        print(f"Owner : {self.owner}")
        print(f"balance : {self.balance}")
        print(f"Account Type : {self.acctype}")
        print(f"Policy Number : {self.policy_number}")
        print('=' * 45)



c1 = BankAccount('Rakesh',2000,"Savings")
c2 = BankAccount('Raam',3000,'Current')
c3 = BankAccount('Rishi',400000000,'Current')
c1.deposit(4000)
c1.withdraw(20000)
c1.get_summary()
h1 = HDFCAccount("Kumar",2000000,'SAVINGS')
h1.withdraw(20000)


i1 = ICICIAccount("Ritish",2000,'SAVINGS')
i1.add_interest()

l1 = LICBank('Deepthi',20000,'LIFE','LIC-12345')
l1.deposit(1000)
l1.withdraw(500)
l1.get_summary()


