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

#for "(a)ction" dialogue. actions and thoughts and stuff, aka the stuff without quotes
define aa = Character("Astin",color="#ff9c3f")
define ea = Character("Elias",color="#a44747")
define pa = Character("Pierre",color="#8f66ca")
define la = Character("Lucas",color="#41a273")
define ja = Character("Jessica",color="#f4acc9")
define na = Character("Nyx",color="#3c3ca1")

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
