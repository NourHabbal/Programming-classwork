import pygame
import os
import math

# Questions:
"""
Why how does this code keep the python program from closing right away?
if __name__ == "__main__":
    main()
"""


def update_window(target):
    pass



# create window and define window name
WIN = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("another game")

def main():
    run = True
    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
    pygame.quit()
if __name__ == "__main__":
    main()



