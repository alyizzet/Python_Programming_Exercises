class Person:
  '''to handle person's details'''
  def __init__(self, fn, ln):
    self.first_name = fn
    self.last_name = ln
    self.address = None #addresses stored as strings
  def set_address(self, adr):
    self.address = adr #strings

class IndividualBankAccount:
  '''to handle individual bank account data'''
  def __init__(self, sort_code, account_number, owner):
    self.sort_code = sort_code
    self.account_number = account_number
    self.owner = owner
    '''TD implement this; creates a bank account
    with sort code as string, account number as string,
    and owner as Person'''
  def set_sort_code(self, sort_code):
    self.sort_code = sort_code
  def get_sort_code(self):
    return self.sort_code
  def set_account_number(self, account_number):
    self.account_number = account_number
  def get_account_number(self):
    return self. account_number
  def get_account_data(self):
    return f'{self.owner.first_name} {self.owner.last_name} {self.sort_code} {self.account_number}'

class SharedBankAccount:
  def __init__(self, sort_code, account_number, owners):
    self.sort_code = sort_code
    self.account_number = account_number
    self.owners = [i for i in owners]

  def set_sort_code(self, sort_code):
    self.sort_code = sort_code
  def get_sort_code(self):
    return self.sort_code
  def set_account_number(self, account_number):
    self.account_number = account_number
  def get_account_number(self):
    return self.account_number
  def get_account_data(self):
    l = []
    for i in range(len(self.owners)):
      l.append(self.owners[i])

    return f'{l[0].first_name} {l[0].last_name}, {l[1].first_name} {l[1].last_name}, {self.sort_code} {self.account_number}'
    