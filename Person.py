class Person:
  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    self.friends = []
    self.greeting_count = 0

  def greet(self, other_person):
    print(f'Hello {other_person.name}, I am {self.name}!')
    self.greeting_count += 1

  def print_contact_info(self):
    print(f'Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}')

  def add_friend(self, other_person):
    self.friends.append(other_person)

  def num_friends(self):
    print(len(self.friends))

  # def greeting_count(self):
  #   print(self.greeting_count)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)
