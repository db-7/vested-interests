# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ast = Character("Astin",color="#ff9c3f")
define eli = Character("Elias",color="#a44747")
define pir = Character("Pierre",color="#8f66ca")
define luc = Character("Lucas",color="#41a273")
define jes = Character("Jessica",color="#f4acc9")
define nyx = Character("Nyx",color="#3c3ca1")

default apts = -10
default epts = -15
default ppts = -20
default lpts = -30
default jpts = -40
default persistent.aend = False
default persistent.eend = False
default persistent.pend = False
default persistent.lend = False
#inventory
init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        def __init__(self, money=10):
            self.money = money
            self.items = []

        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False

        def earn(self, amount):
            self.money += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False

# The game starts here.

label start:

    jump w1
    jump w2
    jump w3
    jump w4
    jump w5

label end:
    if apts > 80:
        jump aend
    elif epts > 85:
        jump eend
    elif ppts > 90:
        jump pend
    elif lpts > 90:
        jump lend
    elif persistent.aend and persistent.eend and persistent.pend and persistent.lend and jpts > 95:
        jump jend
    return
