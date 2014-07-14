class Person:
  """A template for storing people."""

  def __init__(self):
    self.first_name = "Nobody"
    self.last_name = "Smith"
    print("Welcome to the workforce, New Person!")

  def set_fname(self, name):
    self.first_name = name

  def set_lname(self, name):
    self.last_name = name

# Create a new person
# dave = Person()

# This will return "Nobody"
# print(dave.first_name)

# Change his name to "Dave"
# dave.set_fname("Dave")

# This will return "Dave"
# print(dave.first_name)