class Person:
  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone

  def greet(self, other_person):
    print(f'Hello {other_person.name}, I am {self.name}!')

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)
print(f'Name: {sonny.name}\nEmail: {sonny.email}\nPhone: {sonny.phone}')
print(f'Name: {jordan.name}\nEmail: {jordan.email}\nPhone: {jordan.phone}')