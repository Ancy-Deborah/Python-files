
class Car(object):
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    return("started")

  def stop(self):
    return("stopped")

  def accelarate(self):
    return("accelarating...")
    #"accelarator functionality here"

  def change_gear(self, gear_type):
    return("gear changed")
   #" gear related functionality here"


audi = Car("A6", "red", "audi", 80)
print(audi.color)
print(audi.start())
print(audi.accelarate())
print(audi.change_gear(5))
print(audi.stop())