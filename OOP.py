#class blueprint
class Computer:

  #will always get called
  #self refer to the object This is similar to this pointer in C++ and this reference in Java.

  #init is kinda constructor
  def __init__(self, cpu, ram):
    self.cpu = cpu
    self.ram = ram
    
  #objects instance
  def config(self):
    print("config is :", self.cpu, self.ram)

comp1 = Computer('i5', 16)
comp2 = Computer('i7',8)

comp1.config() # we are passing comp1 in config
comp2.config() # we are passing comp2 in config

''''
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print('hey!',self.name) 

p = Person('Pratik')
p.greet()'''
