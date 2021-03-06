﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protag", color="cc0000")
define t = Character("Target", color="ff66ee")
define b = Character("Beau", color="0000cc")
define fa = Character("Friend A", color="00cc00")
define fb = Character("Friend B", color="f0f000")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.



    ##scene bg black

    fb "Wake up, sleepyhead."
    
    p "Hmm?"

    ##scene bg car

    ##show friend a excited
    fa "We’re here. Camping awaits."
    
    p "{i}Yawn{/i}"
    
    ##show target happy
    t "Thanks for driving us all here, Beau!"
    
    ##show beau happy
    b "It’s no worries, I like driving. Especially with you all here coming along."

    return
