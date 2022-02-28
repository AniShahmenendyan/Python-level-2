class BankAccount:
    __rates = {'AMD': 1, 'RUR': 6, 'USD': 500, 'EUR': 600}



    def __init__(self, id, name, currency):
        self.id = id
        self.name = name
        self.balance = 0
        self.currency = currency

    # @property
    # def id(self):
    #     return self.__id
    #
    # @property
    # def name(self):
    #     return self.__name
    #
    # @property
    # def balance(self):
    #     return self.__balance
    #
    # @property
    # def currency(self):
    #     return self.__currency
    #
    # @id.setter
    # def id(self, val):
    #     raise ValueError
    #
    # @name.setter
    # def name(self, val):
    #     raise ValueError
    #
    # @balance.setter
    # def balance(self, val):
    #     raise ValueError
    #
    # @currency.setter
    # def currency(self, val):
    #     raise ValueError


    def credit(self, amount):
        self.balance += amount
        print(f'{self.name} account balance after crediting is: {self.balance} {self.currency}')

    def debit(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'{self.name} account balance after debiting is: {self.balance} {self.currency}')
        else:
            print(f'{self.name} there is no enough money in your account')

    @staticmethod
    def convert(sum1, current_currency, received_currency):
        with_currency_amount = sum1 * BankAccount.__rates[current_currency]
        return with_currency_amount / BankAccount.__rates[received_currency]

    def transfer(self, other, amount):
        if self.balance > amount and self.currency == other.currency:
            self.debit(amount)
            other.credit(amount)
        elif self.balance > amount and self.currency != other.currency:
            self.debit(amount)
            res = BankAccount.convert(amount,self.currency, other.currency)
            other.credit(res)



    def __str__(self):
        return f'{self.name} account balance is {self.balance}'



account1 = BankAccount(123456,'Ani', 'AMD')
account2 = BankAccount(12789,'Anna','USD')

account1.credit(1000)
account1.credit(1000)
account2.debit(200)
account1.transfer(account2,1000)

class SavingAccount(BankAccount):
    def __init__(self, id, name, currency,interest):
        super().__init__(id, name, currency)
        self.interest = interest

    def credit(self, amount):
      super().credit(amount)


    def debit(self,amount):
        super().debit(amount)

    def deposit_after_month(self):
        a = SavingAccount.daily_interest(self.interest, self.balance)
        res = int((a * 30) - (a * 10 / 100))
        BankAccount.credit(self, res)

    @staticmethod
    def daily_interest(interest1, summ):
        result = (summ * interest1 / 100) / 365
        return result

acc1 = SavingAccount(1234567,'Hayk', 'AMD', 10)
acc1.credit(100000)
acc1.deposit_after_month()

class CurrentAccount(BankAccount):
    def __init__(self, id, name, currency,overdraft_limit):
        super().__init__(id, name, currency)
        self.overdraft_limit = overdraft_limit

    def credit(self, amount):
        super().credit(amount)

    def debit(self, amount):
        if amount > self.balance and abs(self.balance - amount) > self.overdraft_limit:
            print('Exceeding the debit amount to your overdarft limit')
        else:
            self.balance -= amount
            print(f'{self.name} account balance is: {self.balance} {self.currency}')


account_current = CurrentAccount(234578,'David','AMD',50000)
account_current.credit(100000)
account_current.debit(110000)