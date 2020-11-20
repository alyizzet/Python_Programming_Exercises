class Counter:
  def __init__(self, my_id):
    self._items = dict()
    self._id = my_id
    self.total_amount = 0
    self.total_price = 0 
    
  def add(self, item_name, amount, price_of_unit):
    self._items[item_name] = [amount,price_of_unit]
    self.total_price += amount * price_of_unit
    self.total_amount += amount

  def remove(self, item_name, amount):
    if item_name in self._items.keys():
        if amount >=self._items[item_name][0]:
            del[self._items[item_name]]
        else:
            self.total_amount -=amount
            self.total_price -= amount*self._items[item_name][1]
    else:
        pass

  def reset(self):
    self.total_amount = 0 
    self.total_price = 0
    self._items.clear()
  
  def get_total(self):
    return self.total_price

  def status(self):
    return f'{self._id} {int(self.total_amount)} {round(self.total_price,2)}'

