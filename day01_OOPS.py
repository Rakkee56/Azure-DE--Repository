class BankAccount:
 
    bank_name = "Azure Bank"                          # Class Variable
 
    def __init__(self, owner, balance=0):
        self.owner    = owner
        self._balance = balance
        print(f"\n Welcome {self.owner}! Account created at {self.bank_name}")
        print("=" * 45)
 
    @property
    def balance(self):                                # Getter
        return self._balance
 
    @balance.setter
    def balance(self, value):                         # Setter with validation
        if not isinstance(value, (int, float)):
            print("Balance must be a number!")
        elif value < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = value
 
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero!")
        else:
            self.balance += amount
            print(f"Deposited ₹{amount} | New Balance: ₹{self.balance}")
 
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero!")
        elif amount > self.balance:
            print(f"Insufficient funds! Available: ₹{self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount} | New Balance: ₹{self.balance}")
 
    def transfer(self, amount, target):
        if amount <= 0:
            print("Amount must be greater than zero!")
        elif amount > self.balance:
            print(f"Insufficient funds! Available: ₹{self.balance}")
        else:
            self.balance         -= amount
            target.balance       += amount
            print(f"{amount} transferred to {target.owner}")
            print(f"   Your Balance         : ₹{self.balance}")
            print(f"   {target.owner}'s Balance : ₹{target.balance}")
 
    def account_details(self):
        print(f"\n{'=' * 45}")
        print(f"   {self.bank_name}")
        print(f"{'=' * 45}")
        print(f"   Owner   : {self.owner}")
        print(f"   Balance : ₹{self.balance}")
        print(f"{'=' * 45}")
 
    def __str__(self):
        return f"BankAccount | {self.owner} | ₹{self.balance}"
 
 
# ============================================================
# CHILD CLASS — Inherits everything from BankAccount
# ============================================================
 
class SavingsAccount(BankAccount):
 
    def __init__(self, owner, balance=0, interest_rate=0.04):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        print(f"   Interest Rate : {self.interest_rate * 100}%")
        print("=" * 45)
 
    def add_interest(self):
        earned           = self.balance * self.interest_rate
        self.balance    += earned
        print(f"\n Interest Applied!")
        print(f"Rate : {self.interest_rate*100}%")
        print(f"Earned : {earned:.2f}")
        print(f"Balance : {self.balance}")
        print("=" * 45)
    
    def account_details(self):
        print("=" * 45)
        print(f"{self.bank_name} - Savings Account")
        print(f"{'=' * 45}")
        print(f"Owner : {self.owner}")
        print(f"Balance : {self.balance}")
        print(f"Rate : {self.interest_rate * 100}%")
        print("=" * 45)
        
    def __str__(self):
        return f"SavingsAccount | {self.owner} | {self.balance:.2f} | Rate : {self.interest_rate * 100}%"
        
    print("=" * 45)
    print(" CLASS AND OBJECT")
    print("=" * 45)
    
    rakesh = BankAccount("Rakesh",10000)
    ravi = BankAccount("Ravi",5000)
    rithvi = BankAccount("Rithvi",80000)
    
    print(f"\nrakesh owner : {rakesh.owner}")
    print(f"rakesh balance : {rakesh.balance}")
    print(f"\nravi owner : {ravi.owner}")
    print(f"ravi balance : {ravi.balance}")
    
    
    print("\n" + "=" * 45)
    print("methods = Deposit,Withdraw,Transfer")
    print('=' * 45)
    
    rakesh.deposit(50000)
    rakesh.withdraw(3000)
    rakesh.withdraw(99999)
    rakesh.deposit(-50000)
    rakesh.transfer(2000,rithvi)
    
    print('=' * 45)
    print("Account Details Method") 
    print('=' * 45)
    
    rakesh.account_details()
    ravi.account_details()
    
    
    print("\n" + "=" * 45)
    print("__str__ - Print Object directly")
    print("=" * 45)
    
    print(rakesh)
    print(ravi)
    
    print("\n" + "=" * 45)
    print("Class Variable - Same for All Objects")
    print("=" * 45)
    
    acc1 = BankAccount("Priya",20000)
    acc2 = BankAccount("Devi",30000)
    
    print(f"\nacc1 bank : {acc1.bank_name}")
    print(f"\nacc2 bank : {acc2.bank_name}")
    
    print("\n" + "=" * 45)
    print("Property Setter and Getter")
    print('=' * 45)
    
    acc = BankAccount("Rakesh",10000)
    
    print(f"Rading Balance : {acc.balance}")
    
    acc.balance = 50000
    
    print(f"Rading Balance After update: {acc.balance}")
    
    acc.balance = -999
    print(f"Rading Balance After -999 update: {acc.balance}")
    
    acc.balance = "hello"
    print(f"Rading Balance After Hello update: {acc.balance}")
    
    print("\n" + "=" * 45)
    print(f"Inheritance - Savings Account")
    print('=' * 45)
    
    savings = SavingsAccount("Rakesh",10000,0.04)
    
    savings.deposit(5000)
    savings.withdraw(2000)
    savings.add_interest()
    savings.account_details()
    print(savings)    
 
