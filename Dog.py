class Dog:

  species = 'mammal'

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def description(self):
    return f'{self.name} is {self.age} years old'

nelson = Dog("Nelson", 3)
print(nelson.description())
print(nelson.species)