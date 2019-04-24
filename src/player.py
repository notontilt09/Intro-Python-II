# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore

class Player:
  def __init__(self, location, items=[]):
    self.location = location
    self.items = items
  
  def show_inventory(self):
    print(Fore.MAGENTA + 'INVENTORY')
    if len(self.items) == 0:
      print(Fore.RED + "You're not carrying any items")
    else:
      for i in self.items:
        print(Fore.YELLOW + "{}: {}".format(i.name, i.description))

  def pick_up(self, item):
    self.items.append(item)
    self.on_pick_up(item)
  
  def drop(self, item):
    self.items.remove(item)
    self.on_drop(item)
  
  def on_pick_up(self, item):
    print(Fore.MAGENTA + '\n You picked up a {}'.format(item.name))

  def on_drop(self, item):
    print(Fore.MAGENTA + '\n You dropped a {}'.format(item.name))