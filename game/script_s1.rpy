
label s1_start:
    
    "It is your first day at a new school. You and your dad have just moved to a new area."    
    char_dad "Ready to go?"

    menu:
        "Yeah":
            char_mc "Yeah, let's go."
        "One more thing":
            char_mc "Wait, just need to grab one more thing."
    
    "You hop into the passger seat next to your dad, anxious about the day ahead."
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

    "You get out of the car, wave goodbye to your dad, and stare up at the building in front of you."
    "Room A430: The room that you'll be going to 5 times per week, for the next year."
    "You find the room with its door wide open."
    "Inside, you can see the teacher behind their desk and one student sitting one row from the front."
    char_teacher "Good Morning! We'll do proper introductions when everyone arrives, feel free to take a seat."
    "As you scan around the room, the other student catches your eye and smiles."
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


    return

label koda_future:
    char_koda "I want to find out how we're even alive, and like how do we even move?"
    char_koda "And I like animals."

    return
