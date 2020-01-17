# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define owner = Character("Owner")
define gf = Character("Mean Lady")
define mom = Character("Lady")
define son = Character("Boy")
define crazy = Character("Crazy Old Lady")
define stray = Character("Stray Cat")
define kitten = Character("Kitten")

# flags

default collar = False
default hungry = True
default stray_friendly = False
default sick = False
default ate_garbage = False

# transitions

define fadehold = Fade(1.0, 1.0, 2.5)

# The game starts here.

label start:
    scene bg start
    with fadehold
    play sound "bird.mp3"
    "Ahhhh!"
    "That was a nice nap…"
menu:
    "Go Right":
        scene bg hallway 2
        with fade
        "Oh yeah! It's time to eat!"
        
menu:
    "Eat from bowl":
        scene bg bowls
        with fade
        "What!? There's nothing here!"
        "What's going on?"
        "I have to let my owner know."
        scene bg argument
        with fade
        gf "It's the third time this week!"
        "Arguing again…"
        "I should say something."
    
menu:
    "Please stop arguing…":
        y "Meow" 
        jump argument
    "Is there anything I can do?":
        y "Meow?"
        jump argument
    "GUYS STOP ARGUING FOR ONCE!":
        y "Meow!"
        jump argument

label argument:
    owner "Look, I'll take care of it later, I need to feed the cat now."
    gf "YOU AND THAT STUPID CAT!"
    owner "What's the problem with the cat?"
    gf "It's always kitty this, kitty that!"
    gf "When are you going to get a job!?"
    gf "We're barely going to make rent this month!"
    gf "She vomits everywhere, rips up the furniture!"
    owner "What do you want me to do?"
    owner "If I put her out she might get hit by a car!"
    gf "I'm not wasting another cent on that thing!"
    gf "WE CAN'T AFFORD—"
    owner "OKAY OKAY!"
    owner "I'll get rid of her…"
    owner "Just give me a moment."
    gf "Fine."
    scene bg black
    owner "Look buddy I wish there was something I could do."
    owner "If I take you to the shelter they're just going to put you down. So you're going to have to try just making it on your own."
    owner "I'm sorry."
    stop music
    jump kicked_out
    
label kicked_out:
    scene bg kicked out
    with fade
    play music "alley.mp3"
menu:
    "Go Left":
        jump big_house
    "Go Right":
        jump alley
    "Cross Street":
        jump car_death

label alley:
    scene bg alley
    with fade
    "Am I really going to have to eat from the dumpster?"
menu:
    "Rummage around dumpster":
        jump trash
    "Go to sleep":
        scene bg sleep street
        with fade
        "This is too much for me."
        "Maybe if I go to sleep this will all go away."
        jump streets_day_2

label trash:
    scene bg dumpster
    with fade
    "Oh god >.<"
    "This is disgusting."
menu:
    "Eat repulsive leftovers":
        scene bg gross
        with fade
        "Oh god."
        $ ate_garbage = True
        $ sick = True
        $ hungry = False
        jump stray_cat_encounter
    "Leave trash can":
        "No, no, I'm not eating this crap"
        jump stray_cat_encounter
        
label stray_cat_encounter:
    scene bg stray
    with fade
    if ate_garbage:
        stray "Did I just see you eat garbage?"
        $ ate_garbage = False 
    stray "You're pretty green aren't you?"
    stray "I know somewhere we can both eat, if you're interested."
menu:
    "Follow stray cat":
        y "Okay, sure."
        y "Why not?"
        stray "Cool."
        $ stray_friendly = True
        jump cat_lady
    "Decline help":
        y "It's okay."
        y "I'll try my luck out here."
        stray "Suit yourself,"
        stray "but it's getting dark out here."
        $ stray_friendly = False
        jump streets_day_2
        
label cat_lady:
    stop music
    scene  bg crazy
    with fade
    play sound "fight.mp3"
    "This place is messy"
    "There are a lot of cats here, kittens too."
    "They all look so sad and hungry."
    "I guess I'm gonna have to sleep here…"
    scene bg sleep crazy
    with fade
    scene bg black
    with fadehold
    stray "Hey, wake up."
    scene bg stray
    stray "Any minute now the old lady is going to come out with food."
    stray "We're going to have to fight the other cats to get any."
    stray "So are you about it, or what?"
menu:
    "Fight":
        y "I guess you have to do what you have to do."
        $ stray_friendly = True
        stray "Let's go then."
        jump fight
    "Flee":
        y "I don't know."
        y "This is more than I bargained for."
        $ stray_friendly = False
        stray "Guess you're not as brave as I thought."
        stray "You should get out of here before it gets crazy"
        jump scraps
        
label fight:
    scene bg before fight
    with fade
    stray "Okay, now's your chance"
    crazy "Good morning kitties!"
    crazy "Breakfast is served"
    scene bg fight
    with hpunch
    play sound "fight.mp3"
    "*hisss*"
    scene bg after fight
    with fade
    if sick:
        stray "Tough break kid, maybe we'll do better next time."
        stray "You might be able to find some scraps by the fish market"
        jump scraps
    else:
        stray "Wow, you did good for yourself"
        jump spoils
        
label spoils:
    stray "Mind sharing some of the spoils?"
menu:
    "Share food with stray":
        jump invitation
    "Keep all the food for yourself":
        stray "Okay, I guess I understand."
        $ stray_friendly = False
        stray "Listen, you better get out of here before the others gang up on you."
        "What am I going to do now?"
        "I guess I have to stay on the streets."
        jump streets_ending

label invitation:
    $ stray_friendly = True
    stray "I think you would do okay here."
    stray "You should stay."
menu:
    "Stay in house":
        jump cat_lady_ending
    "Leave":
        stray "Want to see what else is out there, huh?"
        stray "I understand."
        stray "You might have luck in the fish market."
        jump where_now

label cat_lady_ending:
    scene bg crazy ending
    with fadehold
    "It's hard fighting for food."
    "I miss my owner"
    return

label where_now:
    scene bg alley
    with fade
    play music "alley.mp3"
    "Where should I stay now?"
menu:
    "Stay in the streets":
        jump streets_ending
    "Go to the fish market":
        jump fish_market
    "Try to go home":
        jump owner_rejection

label scraps:
    stop music
    scene bg fish market
    with fade
    "Okay, I guess this is what he was talking about."
    if hungry:
        scene bg fish ending
        with fade
        "It's not much but I'm so hungry."
        $ hungry = False
        "Maybe I can find more food around here."
        jump fish_market
    else:
        "Maybe I can share some of this with the kittens."
        jump to_share_or_not
        
label to_share_or_not:
menu:
    "Share food with kittens":
        "Yea, I think I'll take some of this back to the house."
        jump share
    "Eat all the food":
        "No I should really just eat all of this"
        "Maybe I can find more food around here"
        jump fish_market

label share:
    stop music
    scene bg share food
    with fade
    "Wow, these kittens must have not eaten in days!"
    "They're really scarfing it down."
    kitten "Thanks for feeding us!"
    kitten "Here, I know its not much, but please, take my collar."
    kitten "Maybe you can find a better use for it."
    $ collar = True
    "Wow, my owner would really like this!"
    "I should go home."
    "With this, maybe I can stay…"
    jump home
    
label home:
    stop music
    scene bg acceptance
    with fade
    owner "Hey, you came back!"
    "Huh. Where did the mean lady go?"
    owner "What's that you have there?"
    scene bg best ending
    with fade
    owner "Are those really diamonds?!"
    owner "This could be worth a lot of money!"
    owner "Thanks kitty!"
    y "Meow"
    return

label big_house:
    scene bg smell pie
    with fade
    "Mmm…is that pecan pie?"
    "I wonder where it's coming from."
    scene bg fancy house
    with fade
    stop music
    "Wow!"
    "That's a big house!"
    "That pie is right by the tree too."
menu:
    "Scratch at door":
        jump mom_rejection
    "Climb tree":
        jump tree

label mom_rejection:
    scene bg scratch
    with fade
    play sound "scratch.mp3"
    "*scratch scratch*"
    scene bg rejection
    with fade
    mom "Shoo cat!"
    scene bg fancy house
    with fade
    "What should I do now?"
menu:
    "Climb tree":
        jump tree
    "Sleep in streets":
        jump streets_day_2
    "Go back to house":
        jump owner_rejection

label tree:
    scene bg climb tree
    with fade
    "Nice!"
    "Pie time!"
    "…Wait."
    scene bg see bird
    with fade
    play sound "bird.mp3"
    "Is that a bird up there?"
    "Maybe I can eat it if I climb higher?"
menu:
    "Climb higher":
        jump tree_higher
    "Jump for pie":
        jump pie

label pie:
    scene bg black
    with fade
    "Mmmm…this pie is delicious!"
    $hunger = False
    "Maybe I can stay here…"
menu:
    "Sleep in house":
        jump big_house_day_2
    "Sleep in street":
        jump streets_day_2

label streets_day_2:
    scene bg black
    with fadehold
    stop music
    "Oh man…"
    "That was a rough night…"
    play sound "dog.mp3"
    scene bg dog
    with fadehold
    "A dog!"
    if stray_friendly:
        stray "Over here!"
menu:
    "Run across street":
        jump car_death
    "Follow stray" if stray_friendly:
        jump to_safety

label to_safety:
    scene bg stray
    with fade
    stray "You'll be safe here in the fish market."
    scene bg black
    with fade
    "There's some fish scraps here."
    $ hunger = False
    "It seems like the dog lost interest too."
    jump fish_market

label fish_market:
    scene bg fish market
    with fade
    "Oh look more scraps!"
    "This place isn't so bad."
    "Maybe I should just stay here?"
menu:
    "Stay in fish market":
        jump fish_market_ending
    "Stay in streets":
        "No, maybe I'll be better off on the streets."
        jump street_ending
    "Go back to house":
        "No, I should try going home again."
        jump owner_rejection

label fish_market_ending:
    scene bg fish ending
    with fadehold
    "This place isn't so bad,"
    "but it doesn't feel like home."
    "I miss my owner…"
    return

label big_house_day_2:
    stop music
    scene bg black
    with fadehold
    mom "What are you doing in my house!"
    mom "That's it, I'm taking you to the shelter"
    jump shelter

label tree_higher:
    scene bg bird
    with fade
    "Okay bird, it's dinner time…"
menu:
    "Attack bird":
        jump tree_death
    "Have mercy on bird":
        jump mercy

label mercy:
    "On second thought, I can't do this."
    "Oh no! now I'm stuck!"
    boy "Hello kitty, are you stuck up there?"
    boy "Let me help you down."
    scene bg black
    with fade
    "..."
    $ hunger = False
    scene bg sleep fancy
    with fadehold
    mom "I'm sorry we can't keep the cat."
    boy "Well we can't take her to the shelter, they'll put her down!"
    mom "Okay well, she can't stay here."
    boy "I'm sorry kitty…"
menu:
    "Go back to house":
        jump owner_rejection
    "Stay on streets":
        jump street_ending

label street_ending:
    scene bg black
    with fadehold
    "Man" "We have another stray here!"
    "I'm not a stray, I have an owner!"
    "Why do you keep calling me a stray?"
    jump shelter

label owner_rejection:
    scene bg scratch
    with fade
    play sound "scratch.mp3"
    "*scratch scratch*"
    scene bg rejection
    with fade
    gf "You can't stay here!"
    gf "We can't afford you!"
    gf "Shoo cat!"
    jump kicked_out

label shelter:
    scene bg shelter
    with fadehold
    "What is this awful place?"
    "Man" "I know we just got her in, but no one adopts these older cats."
    "Man" "There's just not enough room for her."
    "I miss my owner."
    jump death

label tree_death:
    scene bg attack bird
    with hpunch
    play sound "fight.mp3"
    "*rawr*"
    scene bg fall
    with hpunch
    play sound "tree break.mp3"
    "Oh no!"
    jump death

label car_death:
    stop music
    scene bg car
    with hpunch
    play sound "car.mp3"
    "*Screeech*"
    scene bg black
    with hpunch
    jump death

label death:
    stop music
    scene bg death
    with fadehold
    owner "Rest in peace kitty…"
menu:
    "Play again":
        jump start
    "Quit":
        return
