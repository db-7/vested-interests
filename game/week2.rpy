label w2:
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
            jump w2back
    n "I will now go get drinks, goodbye."
    scene bg juiceshop with dissolve
    n "ooooh i will now buy juice for boys"
    n "let's see..."
label buyjuice:
    call screen juiceshop
    #if player leaves, the code passes through to here
    n "I don't think I'll get anything."
    "I left the shop and went back to the boys."
    jump w2back
label buyjuice2:
    #if player buys something, jumps here
    "I bought {b}[drink]{/b}, now I have $[inventory.money] left."
    "I left the shop and went back to the boys."
    jump w2back
label w2back:
    if drink == None:
        "I didn't buy anything."
        return
    if route == "Astin":
        n "hey astin i bought you-"
        if drink == "soda":
            a "OH MY GOD I LOVE SODA MARRY ME"
            $ apts += 5
        else:
            a "what is this ew"
    if route == "Elias":
        n "hey elias i bought you-"
        if drink == "juice":
            e "OH MY GOD I LOVE JUICE MARRY ME"
            $ epts += 5
        else:
            e "what is this ew"
    if route == "Pierre":
        n "hey pierre i bought you-"
        if drink == "tea":
            p "OH MY GOD I LOVE TEA MARRY ME"
            $ ppts += 5
        else:
            p "what is this ew"
    if route == "Lucas":
        n "hey lucas i bought you-"
        if drink == "coffee":
            l "OH MY GOD I LOVE COFFEE MARRY ME"
            $ lpts += 5
        else:
            l "what is this ew"
    return