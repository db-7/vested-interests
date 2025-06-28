#Monday - Intro
label w1mon:
    scene mon1 with dissolve
    pause(1.0)
    scene bg bedN with dissolve
    #triple quotes thing needs blank lines between
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
    pause(0.2)

#Tuesday - Meet the Antagonist
label w1tue:
    scene tue1 with dissolve
    pause(1.0)
    scene bg cafe with dissolve
    show nyx neu with dissolve:
        xalign 0.8
    "I enter the bustling cafe and immediately get hit with the smell of bitter coffee and freshly baked bread."
    show nyx hap with dissolve
    "I quickly hear someone call out to me and the jingling of jewelry before I can even turn around."

    show jes hap with moveinleft:
        xalign 0.2
    j "Nyx! It's me Jessica!"

    show nyx neu with dissolve
    "I see a woman with pink hair and gold earrings running up to me."
    "Jessica gives me an eager hug with a sweet smile on her face."

    j "Oh! It's so good to see you! How long has it been? Two or three years?"

    "She quickly leads me to sit at a table with her."
    show jes hap with dissolve:
        xpos 0
        zoom 2.0
    show nyx hap with dissolve:
        xpos 1800
        zoom 2.0
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

    show nyx shr with dissolve
    "I feel confused by her statement, but I brush it off so I could ask a more important question."

    n "So what are your roommates like?"

    show jes ano with MoveTransition(0.5):
        ypos 10
    "For a split second, I thought I saw Jessica's smile drop. A slight grimace forming on her face..."
    show jes neu with MoveTransition(0.1):
        ypos -20
    show jes neu with MoveTransition(0.3):
        ypos 0
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
    show nyx ano with MoveTransition(0.1):
        ypos -50
    show nyx ano with MoveTransition(0.3):
        ypos 0
    "{cps=20}What the hell did she mean by my 'past'?{/cps}"

    n "Excuse me?"

    "Jessica's smile becomes a bit sinister."

    j "Oh, you know~ Just about how you're a homewrecker that likes playing around with people's feelings. We all heard about it back in highschool, right?"

    show nyx neu with dissolve
    "Oh... so that's how it is."
    "Jessica is the same as ever."
    show nyx sch with dissolve
    "I chuckle softly and smirk in amusement."

    n "Oh? Well I really appreciate that, Jessie. Glad I don't have to explain myself to my new roommates. I'm sure we're all gonna get along just fine."

    show nyx hap with moveinright:
        xpos 1700
    "I take Jessica's hands and give them a gentle squeeze."

    show nyx sch with dissolve
    n "You're just so kind-hearted for letting me stay with you even after I 'wronged' you."

    show jes ano with dissolve
    show jes ano with MoveTransition(0.1):
        xpos 50
    show jes ano with MoveTransition(0.1):
        xpos -250
    show jes ano with MoveTransition(0.5):
        xpos 0

    "Jessica scowls and rips her hands away from me."

    j "So you won't even deny it, huh?"

    "She sneers at me."
    "All pretenses have dropped revealing the same snake I knew all too well."

    n "Well how could I when you've set up such a nice story for me? I just hope your lies are better nowadays."

    hide nyx with dissolve
    show nyx neu with dissolve:
        zoom 1.0
        xalign 0.8
    "I stand from my seat and put a five dollar bill down on the table."

    show nyx hap with dissolve
    n "It was nice catching up with you, Jess. You really haven't changed. Buy yourself something nice."

    "I turn to exit the cafe and give Jessica a wave goodbye."

    show nyx sch with dissolve
    n "See you tomorrow, Jessie~"

    hide nyx with moveoutright
    "I can practically feel Jessica's glare burning through my back as I walk out the door."
    
    scene black with dissolve
    pause(0.2)

#Wednesday - Meet the Love Interests
label w1wed:
    scene wed1 with dissolve
    pause(1.0)
    scene bg car with dissolve

    """It's finally time to move in.
    I'm real interested in meeting these guys, especially with whatever bullshit they heard from Jessica.
    I'm sure this will be an entertaining introduction."""

    scene bg apthall with dissolve
    show nyx neu with dissolve:
        xalign 0.8
    """I've arrived at the apartment complex.
    I'm surprised that it's so nice considering the cheap rent I'll be paying.

    I knock on the door and barely have to wait when Jessica quickly swings the door open."""

    show jes hap with Dissolve(0.2):
        xalign 0.2
    show jes hap with MoveTransition(0.2):
        xalign 0.7
    j "Nyx! I'm so happy you're here!"

    """Jessica suddenly embraces me into an almost bone crushing hug.
    I'm about to shove her off of me when I suddenly notice some men in the living room behind her."""
    show nyx neu with moveinright:
        xalign 0.75
    "I quickly adapt and return the hug."

    show nyx hap with moveoutright:
        xalign 0.8
    n "Ah, Jess, you practically knocked me off my feet there."

    show jes hap with moveoutright:
        xalign 0.2
    "Jessica giggles and lets go of me."

    show jes ino with dissolve
    j "I couldn't help it! Even if we saw each other yesterday I still can't believe we'll be living together."
    show jes neu with dissolve
    j "Come on, let me introduce you to your new roommates!"

    scene cg meet with dissolve

    "Jessica gestures towards the cute redhead."

    j "So this is Astin."

    "Astin gives me a small wave."

    a "Yo, I've heard a lot about you from Jessica! Uh, mostly good things."

    "He's quick to correct himself."
    "He seems sweet but I can imagine it's a little hard to be friendly to someone you've only heard awful things about."

    "I give Astin a friendly smile."

    n "I sure hope so. Jessie B. and I have always been real close. It's nice to meet you, Astin."

    "Astin seems to brighten a bit from my laid back demeanor."

    "Then the... extravagantly dressed man decides to introduce himself."

    e "My, My~ I didn't expect our new roommate to be such a stunning woman. My name is Elias, I hope we can get to know each other."

    "Ah... he'd be charming if he was being genuine."

    n "I'm flattered. I'm sure we'll be able to spend plenty of time together."

    e "Perhaps we could-"

    "Jessica quickly interrupts Elias."

    j "Alright, lovebirds. The two of you can flirt later. Anyways, Nyx, this is Pierre."

    "Jessica looks over at the blonde man hoping he would introduce himself."
    "Pierre takes a sip of his tea before speaking softly."

    p "A pleasure to meet you, madame."

    "He seems like a gentleman but a bit quiet."

    j "Pierre isn't really the talkative type but he's charming. You'll get used to it."

    "Jessica then cranes her neck to look over at the stoic man reading on the couch."

    j "Oh and over there is Lucas. He's pretty reserved so you should probably just leave him alone."

    """Lucas doesn't bother to acknowledge my presence or he may not even realize I'm there.

    I can respect wanting to keep to yourself, probably should be grateful I even got to see such a recluse."""

    scene bg aptint with dissolve

    show jes hap with dissolve:
        xalign 0.2
    j "Now that introductions are all done I can tell you about the rules! After that I'll show you around the house."

    show nyx shr with dissolve:
        xalign 0.8
    n "Rules?"

    show jes neu with dissolve
    j "Just normal things really. Everyone has assigned chores each week. You need to be quiet after 8pm. And just respect people's belongings!"

    show jes ino with dissolve
    j "Ah, I almost forgot the most important one. You can't bring anyone over. I know you like to get around and socialize but we prefer to not have guests here."

    show nyx hap with dissolve
    n "Oh, I promise you won't have to worry about that, Jess. People change, you know?"

    "Jessica's eye twitches a bit in irritation."

    show jes ino with dissolve
    j "Of course, I'm sure you have. Come on, let me show you around the house!"

    """Jessica 'eagerly' grabs my hand and leads me away.

    Astin waves me bye as he rushes out of the apartment. He probably has class.

    As soon as we're out of sight from the guys she drops my hand and looks at me with an annoyed expression."""

    show jes ano with dissolve
    j "I see you're already getting pretty friendly. But I recommend you lay off."
    show jes sch with dissolve
    j "I've known these guys for a while and they are wrapped around my little finger. One word from me will have you out of here in a heartbeat."

    "I hold back a laugh."

    n "You really overestimate yourself sometimes. I don't think they're as whipped as you like to think. A snake can shed its skin, but never change its color."

    "Jessica scoffs."

    show jes ano with dissolve
    j "Oh, are you a philosophist now? Spare me the advice, Socrates."

    scene bg bedS with dissolve

    """Jessica finally shows me our shared room.
    Something immediately stands out to me."""

    show nyx shr with dissolve:
        xalign 0.8
    n "Bunk beds? Are you five?"

    "Jessica rolls her eyes."

    show jes neu with dissolve:
        xalign 0.2
    j "Just shut up. You're lucky you even get to sleep in a bed."

    "I raise my hands in a gesture of mock surrender."

    show nyx sch with dissolve
    n "Alright. Alright. No need to blow a fuse."

    "Jessica sighs."

    j "As I said everyone does chores around here. If you don't do your part then you can kiss your ass goodbye."

    n "What's with the hostility? You invite me here and you already want to kick me out? How mean."

    "I say teasingly."

    show jes sch with dissolve
    j "No, no. I don't want to kick you out. That'd be too simple. I want you ruined, I want you to never be able to show your face around campus again."
    j "But I'm not one to rush, perfection takes time."

    n "Well I'm glad your scheming has improved. You utterly failed to manipulate anyone back in highschool."

    show jes ano with dissolve
    j "You're such a bitch."

    n "Takes one to know one, Jessie B."

    j "Don't call me that! Gods, I'm getting out of here. I can't stand you already."

    """Jessica grabs her purse and hurries out of our now shared bedroom.
    So dramatic..."""
    #more like "so adorable <333333"

    """I move in my boxes and unpack, by the time I finish it's already late in the evening.

    I have to go to the clinic tomorrow for my first day so I just hit the hay early.

    I really can't believe I'm sleeping on a bunk bed..."""

    scene black with dissolve
    pause(0.2)
    return

#Thursday - Work
label w1thu:
    scene bg clinicent with dissolve
    show nyx neu with dissolve:
        xalign 0.8
    """I head to the clinic early in the morning to start my training.
    
    The clinic bustles with people going in and out of the many facility rooms.

    The strong scent of antiseptic and bleach permeates the air of the sterile environment.
    
    I stop in front of the receptionist desk to retrieve my ID and scrubs."""

    n "Hello, my name is Nyx. I'm here as a nursing assistant."

    hn "Ah, great. You're here right on time, Miss Nyx. Here's your ID, please change into this pair of scrubs and I'll show you to your station."

    scene bg clinicstation with dissolve

    hn "You'll mainly handle reception duties and giving patients their pills. I'll help you give Mrs. Mason her pills for today and then bring you to the reception desk."

    #-Pill Sorting Minigame Tutorial-

    hn "You did an amazing job, Miss Nyx. I can tell you're made for this job. Please follow me to the receptionist area."

    scene bg clinicent with dissolve

    hn "A nurse receptionist must greet patients, manage appointments, as well as take calls and answer them accordingly. You will mostly handle the calls for training."

    #-Receptionist Minigame-

    hn "Any questions about financial services should go to the billing department. Please transfer the caller to them."

    hn "Mr. Smith needs some medical care. Please send a nurse to his room. Whenever a patient asks about their care, just send a nurse their way."

    hn "This person wants to schedule an appointment. Go ahead and arrange a time for them."

    #-End Tutorial-

    show nyx neu with dissolve:
        xalign 0.8
    hn "You've done a wonderful job in your training today, Miss Nyx. Please discard your scrubs and sanitize your hands when you leave. Have a good night."

    n "Thank you, Nurse Freya. I hope you have a nice shift."

    """Nurse Freya laughs a bit as she waves me bye.

    I suppose that a peaceful night shift at the clinic is unlikely."""

    scene black with dissolve

#Friday - First Solo Encounter
label w1fri:
    scene bg bedS
    """Jessica is already gone by the time I wake up.
    
    It felt nice to sleep in, even if I was worried about Jessica cutting my hair in the midst of my slumber.
    
    I think I want to go out today and explore the area a bit.
    
    Maybe I'll even see some familiar faces.
    
    Where should I go?"""

    menu:
        "Play games at the student computer lab":
            jump CompLabAstin

        "Have a walk around the strip mall":
            jump MallElias

        "Take an extra shift at the clinic":
            jump ClinicPierre

        "Do some reps at the gym":
            jump GymLucas

#Solo Encounters
label CompLabAstin:
    """I might as well walk around campus and stop by the computer lab.

    I think my guild is doing a raid today anyways it'd be fun to beat some noobs."""

    scene bg complab with dissolve
    show nyx neu with dissolve:
        xalign 0.8
    """After a quick look at the campus map I head straight towards the computer lab.

    I grab a seat near the back and login to Last Reverie XIV.

    After a couple practice rounds I head into the guild vs guild raid.

    I target the supports in 'Ghostfire Crusade' and focus on the highest level player called 'BatterUp!'."""

    show ast neu with dissolve:
        xalign 0.2
    a "Ack! No, no, no! Where are the tanks?! NightGoddess is about to kill me!"
    hide ast with dissolve

    """Is that...?

    I glance at the yelling redhead a couple tables ahead of me.

    That's definitely Astin, I didn't know he played MMPORG's too."""

    show ast neu with dissolve:
        xalign 0.2
    a "Are all my teammates afk or something?! The Renegades are going to take over the checkpoint but no one is here!"

    """Well... I may as well have some fun.

    I decided to mess with Astin by targeting him in game.

    I kill his character again."""

    show ast ano with dissolve
    a "How does NightGoddess keep finding me?! I can't even get to the checkpoint before dying!"

    "And again."

    show ast neu with dissolve
    a "Please! Please! Just leave me alone, NightGoddess! Have mercy!"

    "And again."

    show ast ano with dissolve
    a "I quit! I can't do it anymore! My team is useless! You won, NightGoddess. You won..."

    """Astin sighs softly as he leaves the raid and begins to sulk.

    Maybe I went a {i}little{/i} too hard on him.

    Maybe I should message the poor guy."""

    menu:
        "Send him a friend request":
            $ apts += 2
            "I send Astin a friend request and message him in private chat."
            show ast cur with dissolve
            a "Huh? Look behind you?"

            "Astin turns back with a look of confusion before he recognizes me."

            show ast flu with dissolve
            a "Nyx?! Wait, wait, wait. {i}You{/i} were NightGoddess?"

            "Astin takes a seat next to me with an incredulous look on his face."

            show nyx shr with dissolve
            n "Yep. Haven't played Last Reverie in a while so I joined the raid today."
            show ast hap with dissolve
            a "I didn't know you were into gaming! I stood no chance against you the whole time!"
            show nyx neu with dissolve
            n "Nah, your team was the real problem. No one was protecting the supports."

            "Astin groans in annoyance."

            show ast ano with dissolve
            a "I know right? They were all too busy heading into your guild's base and dying!"
            show nyx hap with dissolve
            n "Maybe you should join my guild then. The Renegades are in the Top 500 leaderboard."
            show ast hap with dissolve
            a "Really?! I've just been hopping around guilds trying to find a decent one."
            show nyx sch with dissolve
            n "Yeah, I'll invite you... {i}if{/i} you manage to beat me in a round of PvP."
            show ast tea with dissolve
            a "Oh, you're on!"

            jump endfri1

        "Boast about your win":
            $ apts -= 1
            "not written yet"
            jump endfri1


        "Just keep playing":
            "not written yet"
            jump endfri1
label MallElias:
    """Fortunately, the mall is in a convenient area between my apartment and campus.

    It's big as hell though, what mall needs five whole floors?


    As I window shop a bit and figure out where my favorite stores may be I hear a familiar voice."""

    show eli coc with dissolve:
        xalign 0.2
    e  "And who is this pretty lady I see, hm? Maybe my dearest new roommate?"

    "Elias saunters into my view carrying an expensive looking handbag."

    show nyx neu with dissolve:
        xalign 0.8
    "Ah... Hello, Elias. What a surprise to see you here. I was just window shopping."

    show eli coc with dissolve
    e  "A delightful surprise really. You don't mind if I join you right?"

    show nyx shr with dissolve
    n "Sure. It'd be nice to have some company I guess."

    "Elias smoothly walks by my side as I look around the various stores."

    show eli neu with dissolve
    e "Oh that dress would look wonderful on you. Want me to buy it?"

    "I let out a surprised laugh."

    show nyx shr with dissolve
    "What? You would really buy a dress for someone that you just met?"
    show eli coc with dissolve
    e  "Only for a beauty like you, love."
    show nyx neu with dissolve
    n "I appreciate the thought but no thanks."

    "Elias raises his hands in mock surrender and leaves the idea alone."

    show eli neu with dissolve
    e "Why don't we stop by the food court? It's not too busy around this time."

    "Elias already starts leading me to the food court before I can respond."

    scene black with dissolve
    pause(0.5)
    scene bg foodcourt with dissolve
    "The food court reeked of greasy food while the various chatter coming from the crowd blended into a muted white noise"

    show nyx shr with dissolve:
        xalign 0.8
    n "... Are you even able to eat anything here?"
    show eli cur with dissolve:
        xalign 0.2
    e "What do you mean? The food is fine."
    show nyx neu with dissolve
    n "No. I meant like... you don't seem to be the type that would eat something so pedestrian, I guess."
    show eli hap with dissolve
    e "I like fast food just fine, darling. I'm not that haughty."
    show nyx hap with dissolve
    n "Not sure if I believe that one."
    menu:
        "Offer to buy food":
            $ epts += 1
            show nyx neu with dissolve
            n "I'm getting something from the burger joint over there. Why don't you grab us a table while I place an order?"
            show eli hap with dissolve
            e "Ah of course. Here let me get you my card..."

            "I wave dismissively at Elias."

            show nyx shr with dissolve
            n "Nah, I got it. Is there something specific you want?"
            show eli flu with dissolve
            e "..."
            show eli hap with dissolve
            e "Anything is fine. Just make sure there's no pickles on my burger, love."

            """Elias winks at me before leaving to find a free table.

            Why was he blushing like that? Kinda odd."""

            """I order two cheeseburger combos and look around for Elias while I wait.

            He sits at a table a bit away from me and it seems like...

            Is he staring at me?

            Eh. He's probably just making sure I get everything alright."""

            """I thank the worker that hands me my order on a tray before I head towards Elias.

            He quickly looks away and tries to pretend he wasn't staring at me by turning on his phone."""

            show nyx neu with dissolve
            n "Looking at the weather app or something?"
            show eli flu with dissolve
            e "What? No, of course not. I'm busy... texting someone important."

            "I snort softly and place the tray down in between us."

            show nyx hap with dissolve
            n "Right. I got you a burger, fries, and a cola. No pickles on your burger."
            show eli hap with dissolve
            e "Thanks, doll. I haven't indulged in some junk food for a while."
            n "A college student's diet should consist of at least eighty-five percent pure, processed garbage."
            show eli cur with dissolve
            e "And what about the other fifteen percent?"
            show nyx neu with dissolve
            n "That's the occasional salad when you're feeling guilty and the home cooked meals you get visiting your family."

            "Elias genuinely laughs at my horrible joke."

            show eli hap with dissolve
            e "If you can stay fit like that by eating eighty-five percent junk food then I must be doing something wrong."
            show nyx shr with dissolve
            n "It all depends on the kind of crap you eat. Lots of protein and carbs but minimal sugars and fats."

            "Elias holds up his cheeseburger."

            show eli cur with dissolve
            e "Hm. Then does this count as protein and carbs?"
            show nyx hap with dissolve
            n "Hell yeah it does. Hurry up and eat. I want to check out the rest of the mall."

            "Elias and I end up staying at the mall until late evening and Elias dramatically parts from me."

            show eli coc with dissolve
            e "I'm truly sorry, my sweet, but I must leave you by your lonesome. I have a prior meeting to attend to."

            "I roll my eyes at his antics."

            show nyx neu with dissolve
            n "Just get going, Elias. See you back at the apartment."
            jump endfri1
        "Order your own food":
            "not written yet"
            jump endfri1
label ClinicPierre:
    "While I have the free time I may as well just pick up someone's shift."

    scene bg clinicent with dissolve
    show nyx neu with dissolve:
        xalign 0.8
    "The clinic is bustling as usual and Nurse Freya looks relieved to see me."

    hn "Oh I'm so glad you're here, Miss Nyx. Would you mind helping out some of the patients in the minor injury unit?"
    n "Of course, Nurse Freya. Please try to find some time to take a break, you look quite frazzled."
    hn "I'll sleep when I'm dead. Everything will be fine, dear."

    "Nurse Freya gives me a pat on the back before hurrying to help another patient."

    scene bg clinichall with dissolve
    """In the MIU I help the other nurses with their patients.

    Although it is certainly less busy the unit is also a bit understaffed."""

    #this was "RN"
    "Registered Nurse" "Miss Nyx, would you mind helping out the patient in room 122? He just has a sprained ankle."
    show nyx neu with dissolve
    n "I'll take care of him right away, Nurse Lynn."

    scene bg clinicroom2 with dissolve
    show nyx neu with dissolve:
        xalign 0.8
    "When I enter room 122, I meet a surprisingly familiar face."

    show pir neu with dissolve:
        xalign 0.2
    p "Hello, Madame Nyx. What an unfortunate place for us to meet, non?"

    menu:
        "Remain professional":
            $ ppts += 2
            n "I don't find it too shocking, Mr. Pierre. This is the closest clinic in the area."

            "I move to take a look at Pierre's ankle." 

            n "May I ask how you sprained your ankle, Mr. Pierre? And rate your pain level from one to ten for me."
            p "I was doing some choreography instruction when I landed awkwardly on my foot. The pain is at about a five right now."

            "I nod and write down his responses."

            n "Have you ever sprained this same ankle before?"
            show pir cur with dissolve
            p "Yes, I would say about one or two times now…"
            p "Does that mean there may be something wrong?"
            n "Well, constantly spraining the same ankle can cause permanent damage if the ligaments don't heal correctly." 

            "I roll his ankle around a bit."

            n "Seems to be an inversion sprain. How does it feel when I move it?"
            show pir awk with dissolve
            p "Ah, it's quite tender and uncomfortable."

            "I hand Pierre some ibuprofen and a cup of water."

            n "Please take this, Mr. Pierre. I will bandage your ankle up and apply a brace."

            """Pierre nods and takes the medicine as I requested.

            I carefully wrap gauze around Pierre's ankle, making sure it's tight enough to provide compression before placing a brace around it."""

            n "Alright, you're fine to go home now. You'll need to rest for at least a week and make sure to follow the RICE protocol."
            show pir cur with dissolve
            p "RICE?"

            "I help Pierre stand up before handing him a crutch."

            n "Rest, Ice, Compression, and Elevation."
            n "You can also take some over the counter pain medication like the ibuprofen I gave you."
            n "If you feel like you can't properly put weight on your ankle within two weeks then I would recommend getting it properly looked at by your primary care physician."
            show pir neu with dissolve
            p "Ah, I had never actually known what that stood for. I will heed your advice. Thank you, Nurse Nyx."
            n "Miss Nyx is fine. I am only a nursing assistant so please don't call me ‘Nurse' Take care, Mr. Pierre."

            "The rest of my shift for the night is rather uneventful and I wish the nurses the best before I head home."
            $ inventory.earn(5)
            jump endfri1

        "Act more familiar":
            $ ppts -= 1
            "not written yet"
            $ inventory.earn(5)
label GymLucas:
    """I'll just hit up the gym since I've been slacking a bit.

    I'm pretty sure this apartment complex has a decent fitness center."""

    scene bg gym with dissolve
    show nyx neu with dissolve:
        xalign 0.8
    """The fitness center is an adequate size and has a large variety of equipment.

    It's relatively empty except for two ladies on the treadmills and a man on the bench doing dumbbell presses.

    As I pass the bench press I recognize the man."""

    show nyx shr with dissolve
    n "Lucas? I didn't expect to see you here."

    """Lucas doesn't respond and just continues his dumbbell presses.

    Maybe he didn't hear me because he has headphones in?"""

    menu:
        "Try to start a conversation":
            $ lpts -= 1
            show nyx neu with dissolve
            n "Hey, it's Nyx. Good to see you, Lucas."
            show luc col with dissolve:
                xalign 0.2
            l "..."
            n "I should have realized that you were the type to work out considering your physique. I could spot-"

            "Lucas interrupts me with an annoyed sigh."

            show luc ano with dissolve
            l "Can't you take a hint? Leave me alone."
            show nyx flu with dissolve
            n "Oh, sorry."

            """Lucas moves onto another machine leaving me standing there awkwardly.

            I guess he isn't the type for small talk.

            I shrug it off and do some light stretches before weightlifting."""
            jump endfri1
        "Start working out":
            $ lpts += 1
            """I move onto the leg press machine even though I'm a bit unfamiliar with it.

            As I do some reps I hear Lucas sigh and approach me."""

            show luc ano with dissolve:
                xalign 0.2
            l "Your posture is all wrong. You're going to hurt yourself doing it like that." 

            show nyx shr with dissolve
            n "Really? How? It seems simple enough." 

            "Lucas pulls up the sled and adjusts my legs."

            show luc neu with dissolve
            l "Your feet don't need to be that high. And stop locking out your knees, you're putting stress on the joints."

            "I try my reps again and it does admittedly feel much better."

            show nyx neu with dissolve
            n "Thanks, Lucas."
            l "Don't bother. If you need someone to spot you then come to me."

            "That's surprisingly nice of him."

            n "Ah, yeah. Sure. I can spot you too."

            "Lucas gives me a curt nod before putting his earbuds back in and moves onto another piece of equipment."
            jump endfri1
label endfri1:
    scene black with dissolve
    scene bg aptliving with dissolve

    """It's dark when I get back to the apartment and it seems like everyone's already asleep.
    Then I hear a quiet 'Yo!' Coming from the couch."""

    show ast neu with moveinleft:
        xalign 0.2
    a "Hey, Nyx! You're back pretty late, huh?"

    show nyx neu with moveinright:
        xalign 0.8
    n "Is it that late? I just finished my first shift at the clinic."

    show ast cur with dissolve
    a "The clinic? Ah, I think Jessica mentioned you're a nursing major."
    show ast neu with dissolve
    "I was actually hoping to catch you before you went to bed. Tomorrow we're all having a game night. I figured that you might want to join us but no pressure!"

    show nyx hap with dissolve
    n "Thanks, Astin. I'll be sure to hang out with you all tomorrow."

    show ast hap with dissolve
    a "Great! Uh, have a goodnight, Nyx."
    scene black with dissolve

