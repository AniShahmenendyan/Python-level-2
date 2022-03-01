class BankAccount:
    __rates = {'AMD': 1, 'RUR': 6, 'USD': 500, 'EUR': 600}



    def __init__(self, id, name, currency):
        self._id = id
        self._name = name
        self._balance = 0
        self._currency = currency


    def get_id(self):
        return self._id


    def get_name(self):
        return self._name


    def get_balance(self):
        return self._balance


    def get_currency(self):
        return self._currency


    def id(self, val):
        if type(id) != int:
            raise TypeError
        else:
            self._id = val


    def name(self, val):
        if type(val) != str:
            raise TypeError
        else:
            self._name = val


    def balance(self, val):
        self._balance = val


    def currency(self, val):
        if type(val) != str:
            raise TypeError
        else:
            self._currency = val


    def credit(self, amount):
        self._balance += amount
        print(f'{self._name} account balance after crediting is: {self._balance} {self._currency}')

    def debit(self, amount):
        if self._balance > amount:
            self._balance -= amount
            print(f'{self._name} account balance after debiting is: {self._balance} {self._currency}')
        else:
            print(f'{self._name} there is no enough money in your account')

    @staticmethod
    def convert(sum1, current_currency, received_currency):
        with_currency_amount = sum1 * BankAccount.__rates[current_currency]
        return with_currency_amount / BankAccount.__rates[received_currency]

    def transfer(self, other, amount):
        if self._balance > amount and self._currency == other.get_currency():
            self.debit(amount)
            other.credit(amount)
        elif self._balance > amount and self._currency != other.get_currency():
            self.debit(amount)
            res = BankAccount.convert(amount, self._currency, other.get_currency())
            other.credit(res)



    def __str__(self):
        res1 = BankAccount.convert(self._balance,self._currency,'USD')
        return f'{self._name} account balance is {res1} USD'



account1 = BankAccount(123456,'Ani', 'RUR')
account2 = BankAccount(12789,'Anna','USD')

account1.credit(1000)
account1.credit(1000)
account2.debit(200)
account1.transfer(account2,1000)
# print(str(account1))

class SavingAccount(BankAccount):
    def __init__(self, id, name, currency,interest):
        super().__init__(id, name, currency)
        self._interest = interest

    def credit(self, amount):
      super().credit(amount)


    def debit(self,amount):
        super().debit(amount)

    def deposit_after_month(self):
        a = SavingAccount.daily_interest(self._interest, self._balance)
        res = round((a * 30) - (a * 10 / 100), 2)
        BankAccount.credit(self, res)

    @staticmethod
    def daily_interest(interest1, sum1):
        result = (sum1 * interest1 / 100) / 365
        return result

acc1 = SavingAccount(1234567,'Hayk', 'AMD', 10)
acc1.credit(100000)
acc1.deposit_after_month()

class CurrentAccount(BankAccount):
    def __init__(self, id, name, currency,overdraft_limit):
        super().__init__(id, name, currency)
        self._overdraft_limit = overdraft_limit

    def credit(self, amount):
        super().credit(amount)

    def debit(self, amount):
        if amount > self._balance and abs(self._balance - amount) > self._overdraft_limit:
            print('Exceeding the debit amount to your overdarft limit')
        else:
            self._balance -= amount
            print(f'{self._name} account balance is: {self._balance} {self._currency}')


account_current = CurrentAccount(234578,'David','AMD',50000)
account_current.credit(100000)
account_current.debit(110000)
class Person:
    def __init__(self, name, ssn):
        if type(ssn) == int:
            self.ssn = ssn
        self.name = name

    def __str__(self):
        return self.name

    def __hash__(self):
        return self.ssn

p = Person('Tigran', 123456)
print(p.__hash__())
print(str(p))

class Bank:



    def __init__(self,bank_name):
        self.list_of_account = {}
        self._bank_name = bank_name

    def __getitem__(self, ssn):
        return self.list_of_account[ssn]

    def __setitem__(self, ssn, account):
        if ssn in self.list_of_account.keys():
            self.list_of_account[ssn].append(account)
        else:
            self.list_of_account.update({ssn: [account]})

    # def balance(self, account, balance):
    #     list_of_balances = {}
    #     if account in self.list_of_account.values():
    #        if account not in list_of_balances:
    #            list_of_balances.update({account: balance})
    #     print(list_of_balances)






bank = Bank('converse')
bank[2345] = '1234-2546'
bank[7598] = '213-654'
bank[2345] = '214-564'
# bank.balance('1234-2546', 1000) # չի աշխատում
# print(bank.list_of_account)
