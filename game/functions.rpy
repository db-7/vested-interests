#scripts and stuff
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
                Jump("buyjuice2")
            else:
                return False
                Jump("buyjuice3")

        def earn(self, amount):
            self.money += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False
    inventory = Inventory()

###shop menus###
#styles for confirm
style item_name:
    textalign 0.5
    layout "subtitle"
style item_desc:
    textalign 0.5
    layout "subtitle"

#confirm buy screen
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

                textbutton _("Buy this") action [Function(inventory.buy,item)], Hide("confirmbuy"), Jump("shopend")
                textbutton _("Cancel") action Hide("confirmbuy"), Show("juiceshop")

    ## Right-click and escape answer "no".
    key "game_menu" action Hide("confirmbuy")

#juice shop screen
screen juiceshop:
    imagebutton:
        xalign 0.1 ypos 500
        idle "soda"
        hover "soda_hover"
        action Show("confirmbuy", item=Item("Soda", 5), desc="fizzy juice. $5 (You have [inventory.money])"), SetVariable("drink", "soda")
    imagebutton:
        xalign 0.35 ypos 450
        idle "coffee"
        hover "coffee_hover"
        action Show("confirmbuy", item=Item("Coffee", 5), desc="bean juice. $5 (You have $[inventory.money])"), SetVariable("drink", "coffee")
    imagebutton:
        xalign 0.6 ypos 250
        idle "juice"
        hover "juice_hover"
        action Show("confirmbuy", item=Item("Juice", 5), desc="froot juice. $5 (You have $[inventory.money])"), SetVariable("drink", "juice")
    imagebutton:
        xalign 0.9 ypos 500
        idle "tea"
        hover "tea_hover"
        action Show("confirmbuy", item=Item("Tea", 5), desc="leaf juice. $5 (You have $[inventory.money])"), SetVariable("drink", "tea")
    frame:
        xalign 1.0
        button:
            action Return(), SetVariable("drink", "no")
            #shopend checks for a drink, so we give a pretend drink called "no"
            text "Leave" style "button_text"

#shop end thing
label shopend:
    #avoiding making a new variable 101
    if drink != None:
        if drink == "no":
            "I didn't buy anything."
        else:
            "I bought {b}[drink]{/b}, now I have $[inventory.money] left."
        "I left the shop and went back to the boys."
        jump w2gift
    else:
        "congrats, you broke the game!"

#Pill Sorting Minigame

init python:
    def slider_update(st):
        # SpriteManager update function. Runs when the SpriteManager needs to update.
        # We use this to move the slider from side to side.
        global slider_speed

        for sprite in slider_sprites:
            if sprite.type == "minigame/slider.png":
                if round(sprite.x) < slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
                    sprite.x += slider_speed * pill_difficulty
                    
                elif round(sprite.x) >= slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
                    sprite.direction = "left"
                    slider_speed = 2
                elif round(sprite.x) > 0 and sprite.direction == "left":
                    sprite.x -= slider_speed * pill_difficulty
                    
                elif round(sprite.x) == 0 and sprite.direction == "left":
                    sprite.direction = "right"
                    
        if not stop_slider:
            return 0
        else:
            return None

    def check_slider_safe_zone():
        # Function to check if the user has successfully gotten the timing correct.
        global pill_dispensed
        global pill_dispense_tries
        global stop_slider
        global pillScore

        for slider in slider_sprites:
            if slider.type == "minigame/slider.png":
                for safe_zone in slider_sprites:
                    if safe_zone.type == "minigame/safe-zone.png":
                        if safe_zone.x < slider.x < safe_zone.x + safe_zone_size[0]:
                            # Slider is overlapping the safe-zone. The user has successfully opened the chest.
                            pill_dispensed = True
                            stop_slider = True
                            pillScore += 1
                        elif pill_dispense_tries > 0:
                            # Slider missed the safe-zone. We remove 1 from their attempts.
                            pill_dispense_tries -= 1
                        if pill_dispense_tries == 0:
                            # User used up all their attempts and failed. We show them the game_over screen.
                            renpy.hide_screen("pill_minigame")
                            renpy.show_screen("game_over")
                            stop_slider = True

    def reset_pill_minigame():
        # Function to reset the mini-game so it can be played again.
        global pill_dispensed
        global pill_dispense_tries
        global stop_slider
        global slider_speed

        pill_dispensed = False
        pill_dispense_tries = 2
        stop_slider = False
        slider_speed = 2

        for sprite in slider_sprites:
            if sprite.type == "minigame/slider.png":
                sprite.x = 0
            elif sprite.type == "minigame/safe-zone.png":
                random_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])
                sprite.x = random_x

        slider_SM.redraw(0)
        renpy.restart_interaction()
    
    def total_earnings():
        global pillScore
        global money_earned
        
        if pillScore < 3:
            money_earned == 5
        elif pillScore >= 3:
            money_earned == 10
        elif pillScore >= 7:
            money_earned == 15


transform half_size:
    zoom 0.5

transform pill_transform:
    zoom 0.5
    anchor (0.5, 0.5)
    align (0.5, 0.7)
    subpixel True
    on hover:
        easein 1.0 zoom 0.51
    on idle:
        easein 1.0 zoom 0.5

transform pill_dispensed_anim:
    zoom 0.5
    alpha 0.0
    parallel:
        easein 3.0 zoom 0.7
    parallel:
        easein 2.0 alpha 1.0

screen game_over:
    modal True
    key "mousedown_1" action [Hide("pill_minigame"), Function(reset_pill_minigame), Function(total_earnings), Jump("aftergame")]
    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            background "#FFFFFFE6"
            xfill True
            padding (15, 0)
            align (0.5, 0.5)
            text "Game Over!" color "#000000" size 34 xalign 0.5

screen pill_minigame:
    on "show" action Function(reset_pill_minigame)
    key ["mousedown_1"] action If(pill_dispensed, true = [Hide("pill_minigame", transition = Fade(1, 1, 1)), Show("pill_minigame")], false = Function(check_slider_safe_zone))
    image "minigame/pillgameBG.png" 
    text "Pills Dispensed: [pillScore]"

    if not pill_dispensed:
        frame:
            background "#FFFFFF"
            padding (5, 5)
            align (0.5, 0.3)
            text "Attempts left: [pill_dispense_tries]" size 18 color "#000000" text_align 0.5
        frame:
            background None
            align (0.5, 0.4)
            xysize slider_bar_size
            image "minigame/slider-bar.png" at half_size
            add slider_SM
        image "minigame/pillcup_empty_idle.png" align (0.5, 0.7) at half_size
    else:
        image "minigame/pillcup_full.png" align (0.5, 0.7) at pill_dispensed_anim
        
screen minigame:
    timer 30.0 action Show("game_over")

    image "minigame/pillgameBG.png" at half_size
    #text "Chests Unlocked: [pillScore]"
    
    use pill_minigame
    

label aftergame:

    if pillScore < 5:
        $ money_earned = 5
    elif pillScore >= 5 and < 10:
        $ money_earned = 10
    else:
        $ money_earned = 15


    "After a hard day's work, you have earned $[money_earned]."

    $ inventory.money = money_earned + inventory.money 


    if what_week == 1:
        jump w1thu.afterpill
    elif what_week == 2:
        jump w2tue.afterpill
    elif what_week == 3: 
        jump w3tue.afterpill
