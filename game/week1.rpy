#Monday - Intro
label w1mon:
    scene black with dissolve
    scene bg bedN with dissolve
    """In highschool, Jessica and I were never really in the same circles.\n
    When we occasionally crossed paths we got along just fine. 
    Jessica was always such an upbeat girl, I thought she was sweet.

    When I noticed that Jessica was into one of my friends I tried to help set them up.

    But... Jessica had taken it as an insult. She said I was just 'rubbing it in her face'.
    I didn't know that my friend had a crush on me at the time... but Jessica never gave me the chance to explain.
    
    Instead of the kind girl I knew, Jessica became cold and envious.
    Eventually, rumors about me started to spread.

    'I heard that Nyx has fun leading guys on. She likes seeing them wrapped around her little finger.'
    'Did you hear that Nyx goes after men in relationships? Jessica said that Nyx stole her boyfriend.'

    I didn't mind the whispers and it didn't take long for them to dissipate.
    I was only upset that Jessica would stoop so low to get at me.

    We really could have been good friends...
    
    After highschool, I never heard from Jessica again.

    So a couple years later when I was transferring colleges and looking for a place to stay--\n
    It was really surprising to get an offer from Jessica.

    She mentioned sharing a three bed apartment with four other people and I could stay in her room for cheap.
    Jessica even insisted that we catch up a bit before I officially moved in.
    I figured it was a good deal and worked out the details with her before I started packing the next day.
    
    I'll be meeting her at a cafe tomorrow.
    I think it'll be nice to see her after all this time."""
    scene black with dissolve

#Tuesday - Meet the Antagonist
label w1tue:
    scene bg cafe with dissolve
    show nyx neu with dissolve:
        xalign 0.2
    "I enter the bustling cafe and immediately get hit with the smell of bitter coffee and freshly baked bread."
    show nyx hap with dissolve
    "I quickly hear someone call out to me and the jingling of jewelry before I can even turn around."

    show jes hap with moveinright:
        xalign 0.8
    j "Nyx! It's me Jessica!"

    show nyx neu with dissolve
    "I see a woman with pink hair and gold earrings running up to me."
    "Jessica gives me an eager hug with a sweet smile on her face."

    j "Oh! It's so good to see you! How long has it been? Two or three years?"

    "She quickly leads me to sit at a table with her."
    show nyx hap with dissolve
    "I guess Jessica is still a bubbly whirlwind of energy. She's almost too much for me to keep up with."

    n "Yeah it's been awhile, Jess. You look good, almost didn't recognize you with that pink hair."

    j "I decided to change things up a bit! It looks good right? I really can't believe we're attending the same college now, I'll have to show you around!"

    show nyx neu with dissolve
    n "That'd be nice, Jess. You've always been a good tour guide."

    n "Oh actually, I'm curious about something. What major did you end up getting into? I imagined something on the creative side."

    j "You're surprisingly not far off! I got into photography. I've even won some money from contests!"

    "Jessica begins to ramble about her enthusiasm for photography and I intently listen to her."
    "There's just something about listening to people talk about something they're passionate about."

    show jes neu with dissolve
    j "Oh, I'm sorry I just really went off there didn't I? What's your major then, Nyx?"

    "I wave her off reassuringly."

    n "Nah. You're good, Jess. I'm actually working to become a nurse. Always loved taking care of people."

    j "Hm. That's interesting. I didn't know you were the compassionate type."

    show nyx q with dissolve
    #idk what q is...
    "I feel confused by her statement, but I brush it off so I could ask a more important question."

    n "So what are your roommates like?"

    "For a split second, I thought I saw Jessica's smile drop. A slight grimace forming on her face..."
    "But just as quick as I see it, Jessica smiles sweetly again."
    "Odd."

    show jes ino with dissolve
    j "Well I forgot to mention this before but they're all men actually... I hope that's okay."

    "Jessica feigns a worried look but it's absent of any real concern."

    n "That's alright. Not the first time I've shared a place with some guys."

    show jes hap with dissolve
    "Jessica immediately brightens up."

    j "Just as I would expect from you."

    "That feels like a jab..."
    "This doesn't feel right."
    "But Jessica just continues the conversation normally."

    show jes neu with dissolve
    j "So there's Astin,{w=.5} Elias,{w=.5} Pierre,{w=.5} and Lucas.{w=.5} I think they're all pretty nice."
    j "Lucas is a bit closed off and Elias is kinda flirty. But Pierre is a gentleman and Astin's really funny."

    show nyx neu with dissolve
    "I nod along as I listen to Jessica. They seem like people I could get along with."

    show jes sch with dissolve
    j "And of course I told them about you and your past."

    "{cps=2}...{/cps}"
    show nyx ano with dissolve
    "{cps=20}What the hell did she mean by my 'past'?{/cps}"

    n "Excuse me?"

    "Jessica's smile becomes a bit sinister."

    j "Oh, you know~ Just about how you're a homewrecker that likes playing around with people's feelings. We all heard about it back in highschool, right?"

    show nyx neu with dissolve
    na "Oh... so that's how it is."
    "Jessica is the same as ever."
    show nyx sch with dissolve
    "I chuckle softly and smirk in amusement."

    n "Oh? Well I really appreciate that, Jessie. Glad I don't have to explain myself to my new roommates. I'm sure we're all gonna get along just fine."

    show nyx hap with dissolve
    "I take Jessica's hands and give them a gentle squeeze."

    show nyx sch with dissolve
    n "You're just so kind-hearted for letting me stay with you even after I 'wronged' you."

    show jes ano with dissolve
    show jes ano with MoveTransition(0.1):
        xalign 0.75
    show jes ano with MoveTransition(0.1):
        xalign 0.85
    show jes ano with MoveTransition(0.5):
        xalign 0.8

    "Jessica scowls and rips her hands away from me."

    j "So you won't even deny it, huh?"

    "She sneers at me."
    "All pretenses have dropped revealing the same snake I knew all too well."

    n "Well how could I when you've set up such a nice story for me? I just hope your lies are better nowadays."

    "I stand from my seat and put a five dollar bill down on the table."

    show nyx hap with dissolve
    n "It was nice catching up with you, Jess. You really haven't changed. Buy yourself something nice."

    "I turn to exit the cafe and give Jessica a wave goodbye."

    show nyx sch with dissolve
    n "See you tomorrow, Jessie~"

    hide nyx with moveoutright
    "I can practically feel Jessica's glare burning through my back as I walk out the door."
