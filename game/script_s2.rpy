# Section 2: Diffusion
label s2_start:
    "5 years had gone by and you and Koda were still good friends."
    "Or at least, you thought so; Koda has been acting distant recently."
    "It had been a while since you'd seen each other."

    scene school_front

    "..."
    char_mc "Koda!"
    show char_koda s2 neutral
    char_koda "Oh, hey!"
    char_mc "I haven't seen you in so long, where have you been?"
    char_koda "..."
    char_mc "Are you okay?"
    char_koda "Yeah."
    char_koda "..."
    char_koda "I've been lacking in motivation for a little while though."
    char_koda "I feel ..."
    char_koda "I don't know."

    menu:
        "Let me help you.":
            char_mc "What can I do to help?"
            "Koda stepped back and looked to the ground."
        "But you were so passionate.":
            char_mc "But you were a passionate Biologist, what happened?"
            "Koda's eyes locked to the floor."
        "I'm here if you need.":
            char_mc "No pressure at all, but I'm happy to listen if you need to talk."
            char_koda "I ..."
            "Koda looked away slightly"
            char_koda "Thanks."
            char_koda "I'm not sure I'm ready to talk yet though."
            char_mc "That's okay, take your time."
        "I think therapy might be a good idea":
            char_mc "I think therapy might be a good idea."
            "Koda looked at you in shock."
            char_koda "I don't need therapy."
            char_mc "Sorry, I didn't mean it like that."
            char_koda "I'm going to go."
            hide char_koda

