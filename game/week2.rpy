label w2mon:
    #nope
label w2wed:
    #for testing shop and gifting, tag out later
    menu pickroute:
        "pick a route (for testing)"
        "Astin":
            $ route = "Astin"
        "Elias":
            $ route = "Elias"
        "Pierre":
            $ route = "Pierre"
        "Lucas":
            $ route = "Lucas"
    $ inventory.money = 100
    #
    n "blahblahblah"
    "ooh there's a drink shop"
    menu juiceshopgo:
        "go":
            pass
        "nah":
            jump w2gift
    n "I will now go get drinks, goodbye."
    scene bg juiceshop with dissolve
    n "ooooh i will now buy juice for boys"
    n "let's see..."
label buyjuice:
    call screen juiceshop
    #if player leaves, the code passes through to here
    jump shopend
label w2gift:
    if drink == "no":
        jump w2wedcon
    elif route == "Astin":
        n "hey astin i bought you-"
        if drink == "soda":
            a "OH MY GOD I LOVE SODA MARRY ME"
            $ apts += 5
        else:
            a "what is this ew"
    elif route == "Elias":
        n "hey elias i bought you-"
        if drink == "juice":
            e "OH MY GOD I LOVE JUICE MARRY ME"
            $ epts += 5
        else:
            e "what is this ew"
    elif route == "Pierre":
        n "hey pierre i bought you-"
        if drink == "tea":
            p "OH MY GOD I LOVE TEA MARRY ME"
            $ ppts += 5
        else:
            p "what is this ew"
    elif route == "Lucas":
        n "hey lucas i bought you-"
        if drink == "coffee":
            l "OH MY GOD I LOVE COFFEE MARRY ME"
            $ lpts += 5
        else:
            l "what is this ew"
label w2wedcon:
    n "anyways"
    n "blahblahblah"