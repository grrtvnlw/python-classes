class Dog:

  species = 'mammal'

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
nelson = Dog("Nelson", 3)
print(nelson.species)