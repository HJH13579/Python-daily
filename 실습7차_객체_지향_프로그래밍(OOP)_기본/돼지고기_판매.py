
class Pig():

  def __init__(self, stock, price):
    self.stock = stock
    self.price = price


  def for_sale(self, amount):

    sale_price = self.price * amount * 0.8

    self.stock = self.stock - amount

    return sale_price, self.stock

  @classmethod
  def original_price(self, amount):

    origin_price = self.price * amount
  
    return origin_price


b_pig = Pig(100, 1000)

print(b_pig.for_sale(50))
print(b_pig.original_price(50))
  
