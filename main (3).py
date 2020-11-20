class Person:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None #addresses stored by strings
    def set_address(self, adr):
        self.address = adr #strings

class BankAccount:
    def __init__(self, sort_code, account_number):
      self.sort_code = sort_code
      self.account_number = account_number
    def set_sort_code(self, sort_code):
      self.sort_code = sort_code

    def get_sort_code(self):
      return self.sort_code

    def set_account_number(self, account_number):
      self.account_number = account_number

    def get_account_number(self):
      return self.account_number
  
    def get_account_data(self):
      return f'{self.sort_code} {self.account_number}'

class IndividualBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owner):
        super().__init__(sort_code, account_number)
        self.owner = Person(owner.first_name,owner.last_name)

    def get_account_data(self):
        return f'{self.owner.first_name} {self.owner.last_name} {self.sort_code} {self.account_number}'

class SharedBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owners):
        super().__init__(sort_code, account_number)
        self.l = []
        for i in range(len(owners)):
          self.l.append(owners[i])
    def get_account_data(self):
      return f'{self.l[0].first_name} {self.l[0].last_name}, {self.l[1].first_name} {self.l[1].last_name}, {self.sort_code} {self.account_number}'
