import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("le game") 

WHITE = (255, 255, 255)

framerate = 60



SPRITE_WIDTH, SPRITE_HEIGHT = 50, 80
SPRITE_IMAGE1 = pygame.image.load(os.path.join("pygame introduction/asset/sprite1.png"))
SPRITE1 = pygame.transform.rotate(pygame.transform.scale(SPRITE_IMAGE1, (SPRITE_WIDTH, SPRITE_HEIGHT)), 180 )

SPRITE_IMAGE2 = pygame.image.load(os.path.join("pygame introduction/asset/sprite2.png"))
SPRITE2 = pygame.transform.rotate(pygame.transform.scale(SPRITE_IMAGE2, (SPRITE_WIDTH, SPRITE_HEIGHT)), 0 )

def update_window(one, two):
    WIN.fill((WHITE))
    WIN.blit(SPRITE1, (one.x, one.y))
    WIN.blit(SPRITE2, (two.x, two.y))

    pygame.display.update()

def main():
    player_one = pygame.Rect(100, 300,SPRITE_WIDTH, SPRITE_HEIGHT)
    player_two = pygame.Rect(600, 300,SPRITE_WIDTH, SPRITE_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #LEFT
            player_one.x -= 1
        elif keys_pressed[pygame.K_s]: #DOWN
            player_one.y += 1
        elif keys_pressed[pygame.K_w]: #UP
            player_one.y -= 1
        elif keys_pressed[pygame.K_d]: #RIGHT
            player_one.x += 1


        if keys_pressed[pygame.K_j]: #LEFT
            player_two.x -= 1
        elif keys_pressed[pygame.K_k]: #DOWN
            player_two.y += 1
        elif keys_pressed[pygame.K_i]: #UP
            player_two.y -= 1
        elif keys_pressed[pygame.K_l]: #RIGHT
            player_two.x += 1

        #player_one.x += 1
        update_window(player_one, player_two)
 
    pygame.quit()
if __name__ == "__main__":
    main()