#class
class Computer:

  #will always get called
  #sef refer to the object
  def __init__(self, cpu, ram):
    self.cpu = cpu
    self.ram = ram
    
  #objects
  def config(self):
    print("config is :", self.cpu, self.ram)

comp1 = Computer('i5', 16)
comp2 = Computer('i7',8)

comp1.config() # we are passing comp1 in config
comp2.config() # we are passing comp2 in config
