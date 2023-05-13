import pygame
import os
import math

# Questions:
"""
Why how does this code keep the python program from closing right away?
if __name__ == "__main__":
    main()
"""

"""
THE PLAN:
Create a maze game
    features
        



"""



def update_window(target):
    if target == "background":
        pass
    elif target == "player":
        pass
    elif target == "":
        pass
    elif target == "":
        pass

    """POSSIBLE TARGET VALUES
    -------------------------
    1. background
    2. player
    3. NPC
    4. projectiles
    5. 
    
    
    """
    
    
    pass

WINDOW_SIZE = { #for the sake of organization
    "width": 1000,
    "height": 750
}

# create window and define window name
WINDOW_DISPLAY = pygame.display.set_mode((WINDOW_SIZE["width"], WINDOW_SIZE["height"]))
pygame.display.set_caption("another game")

def main():
    run = True
    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False 
        # check all pygame events, and when pressing the quit (x) button, close the window

    pygame.quit()
if __name__ == "__main__":
    main()



