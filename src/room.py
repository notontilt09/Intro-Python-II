# Implement a class to hold room information. This should have name and
# description attributes.
from colorama import Fore

class Room:
  def __init__(self, name, description, items=[]):
    self.name = name
    self.description = description
    self.items = items
  
  def show_items(self):
    if len(self.items) == 0:
      print(Fore.RED + 'Room has no items')
    else:
      for i in self.items:
        print(Fore.YELLOW + '{}: {}'.format(i.name, i.description))
  
  def remove_item(self, item):
    self.items.remove(item)
  
  def receive_item(self, item):
    self.items.append(item)



