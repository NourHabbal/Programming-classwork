import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("le game") 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MOVE_SPEED = 3

BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)
FPS = 60


PLAYER_WIDTH, PLAYER_HEIGHT = 50, 80

SPRITE_IMAGE1 = pygame.image.load(os.path.join("pygame introduction/asset/sprite1.png"))
SPRITE_IMAGE2 = pygame.image.load(os.path.join("pygame introduction/asset/sprite2.png"))

SPRITE_EDIT1 = pygame.transform.rotate(pygame.transform.scale(SPRITE_IMAGE1, (PLAYER_WIDTH, PLAYER_HEIGHT)), 180 )
SPRITE_EDIT2 = pygame.transform.rotate(pygame.transform.scale(SPRITE_IMAGE2, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0 )

def draw_window(one, two):
    WIN.fill((WHITE))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(SPRITE_EDIT1, (one.x, one.y))
    WIN.blit(SPRITE_EDIT2, (two.x, two.y))
    pygame.display.update()

def handle_movement_one(keys_pressed, player_given):
    if keys_pressed[pygame.K_a] and player_given.x - MOVE_SPEED > 0: #LEFT
        player_given.x -= MOVE_SPEED
    if keys_pressed[pygame.K_s] and player_given.x + MOVE_SPEED + player_given.height < HEIGHT - 5: #DOWN
        player_given.y += MOVE_SPEED
    if keys_pressed[pygame.K_w] and player_given.y - MOVE_SPEED > 0: #UP
        player_given.y -= MOVE_SPEED
    if keys_pressed[pygame.K_d] and player_given.x + MOVE_SPEED + player_given.width < BORDER.x: #RIGHT
        player_given.x += MOVE_SPEED

def handle_movement_two(keys_pressed, player_given):
    if keys_pressed[pygame.K_j]: #LEFT
        player_given.x -= MOVE_SPEED
    if keys_pressed[pygame.K_k]: #DOWN
        player_given.y += MOVE_SPEED
    if keys_pressed[pygame.K_i]: #UP
        player_given.y -= MOVE_SPEED
    if keys_pressed[pygame.K_l]: #RIGHT
        player_given.x += MOVE_SPEED

def main():
    player_one = pygame.Rect(100, 300,PLAYER_WIDTH, PLAYER_HEIGHT)
    player_two = pygame.Rect(700, 300,PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        handle_movement_one(keys_pressed, player_one)
        handle_movement_two(keys_pressed, player_two)


        draw_window(player_one, player_two)
 
    pygame.quit()
if __name__ == "__main__":
    main()

