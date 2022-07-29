class Tab:

  menu = {
    'wine':5,
    'beer':3,
    'soft_drink':2,
    'wings':10,
    'burger':14,
    'salad':12,
    'desert':6,
    'tacos':8,
  }

  def __init__(self):
    self.total = 0
    self.items = [ ]

  def add(self,item):
    self.items.append(item)
    self.total += self.menu[item]

  def print_bill(self,tax,service):
    tax = (tax/100)*self.total
    service = (service/100) * self.total
    total = self.total + tax + service

    for item in self.items:
      print(f'{item} ${self.menu[item]}')

    print(f'{"Total":20} ${total:.2f}')