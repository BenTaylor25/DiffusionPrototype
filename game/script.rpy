define mc = Character("[username]")
define dad = Character("Dad")


label start:
    python:
        username = renpy.input("Enter name: ", length=32).strip()

        if not username:
            username = "Ben"

    scene bg room
    show mc happy

    dad "hi"
    mc "hi"

    return
