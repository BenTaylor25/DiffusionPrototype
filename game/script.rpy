define char_mc = Character("[mc_name]")
define char_dad = Character("Dad")
define char_koda = Character("Koda")
define char_teacher = Character("Teacher")

label start:
    python:
        mc_name = renpy.input("Enter name: ", length=32).strip()

        if not mc_name:
            mc_name = "Ben"

    call s1_start

    return
