# Section 2: Diffusion
label s2_start:
    "5 years had gone by and you and Koda were still good friends."
    "Or at least, you thought so; Koda has been acting distant recently."
    "It had been a while since you'd seen each other."

    scene bg school_front

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
            char_koda "I'm just going to go home."
        "But you were so passionate.":
            char_mc "But you were a passionate Biologist, what happened?"
            "Koda's eyes locked to the floor."
            char_koda "I'm just going to go home."
        "I'm here to listen if you need.":
            char_mc "No pressure at all, but I'm happy to listen if you need to talk."
            char_koda "I ..."
            "Koda looked away slightly"
            char_koda "Thanks."
            char_koda "I'm not sure I'm ready to talk yet though."
            char_mc "That's okay, take your time."
            char_koda "I'm going to head home, but can I call you later?"
            char_mc "Of course."

    scene blank
    with fade

    return
