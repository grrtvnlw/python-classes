class Person:
  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    self.friends = []
    self.greeting_count = 0
    self.greets = {}

  def __str__(self):
    return f'Person: {self.name} {self.email} {self.phone}'

  def greet(self, other_person):
    if other_person.name not in self.greets.keys():
      self.greets[other_person.name] = 1

    print(f'Hello {other_person.name}, I am {self.name}!')
    self.greeting_count += 1

  def print_contact_info(self):
    print(f'Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}')

  def add_friend(self, other_person):
    self.friends.append(other_person)

  def num_friends(self):
    print(len(self.friends))

  def num_unqiue_people_greeted(self):
    print(len(self.greets))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
dee_ann = Person('Dee_Ann', 'd@gmail.com', '555-867-5309')

sonny.num_unqiue_people_greeted()
sonny.greet(jordan)
sonny.num_unqiue_people_greeted()
sonny.greet(jordan)
sonny.num_unqiue_people_greeted()
sonny.greet(dee_ann)
sonny.num_unqiue_people_greeted()
