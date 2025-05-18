#screens, but in a seperate file from the one provided by ren'py
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
    inventory = Inventory()

style item_name:
    textalign 0.5
    layout "subtitle"
style item_desc:
    textalign 0.5
    layout "subtitle"
screen confirmbuy(item, desc):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(item.name):
                style "item_name"
                xalign 0.5
            label _(desc):
                style "item_desc"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Buy this") action [Function(inventory.buy,item), Hide("confirmbuy")]
                textbutton _("Cancel") action Hide("confirmbuy")

    ## Right-click and escape answer "no".
    key "game_menu" action Hide("confirmbuy")

screen juiceshop:
    imagebutton:
        xalign 0.1 ypos 500
        idle "soda"
        hover "soda_hover"
        action Show("confirmbuy", item=Item("Soda", 5), desc="fizzy juice. $5 (You have [inventory.money])")
    imagebutton:
        xalign 0.35 ypos 450
        idle "coffee"
        hover "coffee_hover"
        action Show("confirmbuy", item=Item("Coffee", 5), desc="bean juice. $5 (You have $[inventory.money])")
    imagebutton:
        xalign 0.6 ypos 250
        idle "juice"
        hover "juice_hover"
        action Show("confirmbuy", item=Item("Juice", 5), desc="froot juice. $5 (You have $[inventory.money])")
    imagebutton:
        xalign 0.9 ypos 500
        idle "tea"
        hover "tea_hover"
        action Show("confirmbuy", item=Item("tea", 5), desc="leaf juice. $5 (You have $[inventory.money])")