# Section 1: Introductions
label s1_start:
    scene bg mc_house

    "It is your first day at a new school. You and your dad have just moved to a new area."
    show char_dad neutral
    char_dad "Ready to go?"

    menu:
        "Yeah":
            char_mc "Yeah, let's go."
        "One more thing":
            char_mc "Wait, just need to grab one more thing."

    scene bg in_car
    show char_dad neutral
    
    "You hop into the passenger seat next to your dad, anxious about the day ahead."
    char_dad "How you feeling?"

    menu:
        "Excited":
            char_mc "Excited, I can't wait to meet new people."
            char_dad "Nice one, you're going to have a great time."
        "Nervous":
            char_mc "Nervous, there are going to be so many new people."
            char_dad "It's okay to feel like that, but you'll do fine, promise."
        "Meh":
            char_mc "Meh, I'll see how it goes."
            char_dad "Come on, it'll be fun."

    scene bg school_front

    "You get out of the car, wave goodbye to your dad, and stare up at the building in front of you."
    "Room A430: The room that you'll be going to 5 times per week, for the next year."

    scene bg school_classroom

    "You find the room with its door wide open."
    "Inside, you can see the teacher behind their desk and one student sitting one row from the front."

    show char_teacher neutral
    char_teacher "Good Morning! We'll do proper introductions when everyone arrives, feel free to take a seat."
    hide char_teacher neutral

    show char_koda neutral
    "As you scan the room, the other student catches your eye and smiles."
    "You sit down in the seat next to them."
    char_koda "Hi, my name is Koda, nice to meet you."
    char_mc "Hi, I'm [mc_name]."
    "You notice a book on the desk in front of Koda: 'Intro to Biology'."
    "Koda sees you looking and smiles."
    char_koda "I want to be a biologist when I'm older!"

    $ same_career = False
    menu:
        "Cool":
            char_mc "That's Cool!"
            char_koda "Yeah!"
            call koda_future
        "Me too":
            $ same_career = True
            char_mc "Hey, me too!"
            char_koda "Woah, really?"
        "Why?":
            char_mc "Why do you want to be a biologist?"
            char_koda "Well:"
            call koda_future

    if same_career:
        char_koda "What area of biology are you most interested in?"
        menu:
            "Physiology":
                char_mc "Physiology is cool."
                char_koda "Yeah, I love that too! Especially animal physiology."
            "Zoology":
                char_mc "I like Zoology."
                char_koda "I love zoology! Especially animal physiology."
            "Botany":
                char_mc "Botany is my favourite."
                char_koda "Plants are cool! I prefer animal physiology personally."
            "I don't know":
                char_mc "I don't really have a favourite. Not yet at least."
                char_koda "That's okay! I recommend animal physiology."
    else:
        char_koda "Do you know what you want to do when you're older?"
        menu:
            "Something Technical":
                char_mc "Something technical. I want to create something new."
                char_koda "Cool! I can't wait to see your creation!"
            "Something Scientific":
                char_mc "Something scientific. I want to discover something new."
                char_koda "Cool! There's plenty more to discover!"
            "Something Creative":
                char_mc "Something creative. I love art, and I want to create something new."
                char_koda "Cool! I look forward to seeing your creation!"
            "Something Physical":
                char_mc "Something physical. I want a job that'll keep me in good shape."
                char_koda "Cool! That's really smart!"
            "I don't know":
                char_mc "I don't know yet."
                char_koda "That's okay. I'm sure you'll figure it out!"
    hide char_koda

    "Before you know it, the rest of the class had arrived."
    "You and Koda shared a lot of classes that year and became good friends."

    return

label koda_future:
    char_koda "I want to find out how we're even alive, and like how do we even move?"
    char_koda "And I like animals."
    char_koda "Plants are cool too."

    return
