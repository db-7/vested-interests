# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#for dialogue with quotes
define a = Character("Astin",color="#ff9c3f", what_prefix="\"", what_suffix="\"")
define e = Character("Elias",color="#a44747", what_prefix="\"", what_suffix="\"")
define p = Character("Pierre",color="#8f66ca", what_prefix="\"", what_suffix="\"")
define l = Character("Lucas",color="#41a273", what_prefix="\"", what_suffix="\"")
define j = Character("Jessica",color="#f4acc9", what_prefix="\"", what_suffix="\"")
define n = Character("Nyx",color="#3c3ca1", what_prefix="\"", what_suffix="\"")

define hn = Character("Head Nurse", what_prefix="\"", what_suffix="\"")

default apts = -10
default epts = -15
default ppts = -20
default lpts = -30
default jpts = -40
default route = None
default persistent.aend = False
default persistent.eend = False
default persistent.pend = False
default persistent.lend = False
default inventory.money = 0
default drink = None

#minigame related variables
default pillScore = 0
default money_earned = 0
default what_week = 1

$ slider_SM = SpriteManager(update = slider_update)
$ slider_sprites = []

# Safe zone variables
$ safe_zone_image = Image("safe-zone.png")
$ safe_zone_transform = Transform(child = safe_zone_image, zoom = 0.5)
$ safe_zone_size = (int(149 / 2), int(70 / 2))
$ slider_sprites.append(slider_SM.create(safe_zone_transform))
$ slider_sprites[-1].type = "safe-zone"

# Slider variables
$ slider_bar_size = (int(545 / 2), int(70 / 2))
$ slider_image = Image("slider.png")
$ slider_transform = Transform(child = slider_image, zoom = 0.5)
$ slider_sprites.append(slider_SM.create(slider_transform))
$ slider_sprites[-1].type = "slider"
$ slider_sprites[-1].direction = "right"
$ slider_size = (int(48 / 2), int(66 / 2))
$ slider_speed = 1
$ stop_slider = False

# Chest variables
$ pill_dispensed = False
$ pill_dispense_tries = 2
$ pill_difficulty = 1


# The game starts here.

label start:
    jump w1mon
    jump w2mon
    jump w3mon
    jump w4mon
    jump w5mon

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
