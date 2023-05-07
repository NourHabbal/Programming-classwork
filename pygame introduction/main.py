import pygame
import os
import math

pygame.font.init()
pygame.mixer.init()

#CHANGES MADE:
# + Made it so that the lower the health a player has the faster they will be. this uses the function y = 2^{-x+3}+1. (Thank Precalus 12 for this knowledge :) )
#   y is the speed and x is the current health of the given player, the variable MOVE_SPEED has been replaced by this function

# + background png has been replaced with a less plain background
# + player sprites are beig planned
# + window sizes have been altered
# + custom sound effects used, which have been randomly generated with the online tool jfxr
# + changed game title
# + use buttons WASP to move player one, IJKL to move player two, and use left/right alt buttons to shoot 
# + rotated barrier
# + modified hp and winner text messages displayed


# TO BE ADDED
# Create sprites
# rotate sprites for vertical changes


"""
This project was created with python versions 3.11.3 and 3.9.x 
"""

#-------------------

WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("le game") 

BULLET_SHOOT_SOUND = pygame.mixer.Sound(os.path.join("pygame introduction", "asset", "Explosion 2.mp3"))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("pygame introduction", "asset", "Explosion 1.mp3"))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


DISPLAY_HP_FONT = pygame.font.SysFont("comicsans", 40)
DISPLAY_WINNER_FONT = pygame.font.SysFont("comicsans", 100)

#BORDER = pygame.Rect(WIDTH//2, 0, 10, HEIGHT) # CHANGE FOR VERTICAL MOD
COLLISION = pygame.Rect(0,HEIGHT//2, WIDTH, 10)

FRAMERATE = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 70, 80
BULLET_SPEED = 7
BULLET_MAX = 5

PLAYER_ONE_HIT = pygame.USEREVENT + 1
PLAYER_TWO_HIT = pygame.USEREVENT + 2

PLAYER_ONE_HEALTH = 9
PLAYER_TWO_HEALTH = 9


SPRITE_IMAGE_SOURCE1 = pygame.image.load(os.path.join("pygame introduction", "asset", "sprite1.png"))
SPRITE_IMAGE_SOURCE2 = pygame.image.load(os.path.join("pygame introduction", "asset", "sprite2.png"))

SPRITE_EDIT1 = pygame.transform.rotate(pygame.transform.scale(SPRITE_IMAGE_SOURCE1, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0 ) # CHANGE FOR VERTICAL MOD
SPRITE_EDIT2 = pygame.transform.rotate(pygame.transform.scale(SPRITE_IMAGE_SOURCE2, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0 ) # CHANGE FOR VERTICAL MOD

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("pygame introduction", "asset", "background.png")), (WIDTH, HEIGHT))



def draw_window(one, two, one_bullets, two_bullets, player_health_one, player_health_two):
    WIN.blit(BACKGROUND, (0,0))
    #pygame.draw.rect(WIN, BLACK, BORDER) #old
    pygame.draw.rect(WIN, BLACK, COLLISION)

    WIN.blit(SPRITE_EDIT1, (one.x, one.y))
    WIN.blit(SPRITE_EDIT2, (two.x, two.y))
    player_one_text = DISPLAY_HP_FONT.render("P1 - HP: " + str(player_health_one), 1, WHITE)
    player_two_text = DISPLAY_HP_FONT.render("P2 - HP: " + str(player_health_two), 1, WHITE)

    WIN.blit(player_two_text, (WIDTH - player_one_text.get_width() - 10, 10))
    WIN.blit(player_one_text, (10, 10))

    for bullet in one_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in two_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def handle_movement_one(keys_pressed, player_given):
    # MOVE_SPEED = 2^{-x+3}+1, where x = given player health. 
    MOVE_SPEED = (2**(-PLAYER_ONE_HEALTH + 4) + 1) 

    if keys_pressed[pygame.K_a] and player_given.x - MOVE_SPEED > 0:  # LEFT
        player_given.x -= MOVE_SPEED
    if keys_pressed[pygame.K_d] and player_given.x + MOVE_SPEED + player_given.width < WIDTH:  # RIGHT
        player_given.x += MOVE_SPEED
    if keys_pressed[pygame.K_w] and player_given.y - MOVE_SPEED > 0:  # UP
        player_given.y -= MOVE_SPEED
    if keys_pressed[pygame.K_s] and player_given.y + MOVE_SPEED + player_given.height < HEIGHT//2:  # DOWN
        player_given.y += MOVE_SPEED

def handle_movement_two(keys_pressed, player_given):
    MOVE_SPEED = (2**(-PLAYER_TWO_HEALTH + 4) + 1) 

    if keys_pressed[pygame.K_j] and player_given.x - MOVE_SPEED > 0: #LEFT
        player_given.x -= MOVE_SPEED
    if keys_pressed[pygame.K_l] and player_given.x + MOVE_SPEED + player_given.width < WIDTH: #RIGHT
        player_given.x += MOVE_SPEED
    if keys_pressed[pygame.K_i] and player_given.y - MOVE_SPEED + COLLISION.height - 0 > HEIGHT//2: #UP
        player_given.y -=MOVE_SPEED
    if keys_pressed[pygame.K_k] and player_given.y + MOVE_SPEED + player_given.height//2 < HEIGHT: #DOWN
        player_given.y += MOVE_SPEED

def handle_bullets(player_one_bullets, player_two_bullets, player_one, player_two):
    for i in player_one_bullets:
        i.y += BULLET_SPEED
        if player_two.colliderect(i):
            pygame.event.post(pygame.event.Event(PLAYER_TWO_HIT))
            player_one_bullets.remove(i)
        elif i.y > WIDTH: #outside barrier
            player_one_bullets.remove(i)

    for i in player_two_bullets:
        i.y -= BULLET_SPEED
        if player_one.colliderect(i):
            pygame.event.post(pygame.event.Event(PLAYER_ONE_HIT))
            player_two_bullets.remove(i)
        elif i.y < 0: #outside barrier
           player_two_bullets.remove(i)


def draw_winner(text):
    draw_text = DISPLAY_WINNER_FONT.render("the winner is...", 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)
    draw_text = DISPLAY_WINNER_FONT.render(text, 1, WHITE)
    WIN.fill(BLACK)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    player_one = pygame.Rect(WIDTH//2, HEIGHT//4,PLAYER_WIDTH, PLAYER_HEIGHT) # CHANGE PLAYER ONE STARTING LOCATION
    player_two = pygame.Rect(WIDTH//2, HEIGHT*(0.75),PLAYER_WIDTH, PLAYER_HEIGHT) # CHANGE PLAYER TWO STARTING LOCATION

    player_one_bullets = []
    player_two_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FRAMERATE)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LALT and len(player_one_bullets) < BULLET_MAX:
                    bullet = pygame.Rect(player_one.x + player_one.width//2, player_one.y + player_one.height, 10, 10 )
                    player_one_bullets.append(bullet)
                    BULLET_SHOOT_SOUND.play()

                if i.key == pygame.K_RALT and len(player_two_bullets) < BULLET_MAX:
                    bullet = pygame.Rect(player_two.x + player_two.width//2, player_two.y, 10, 10 )
                    player_two_bullets.append(bullet)
                    BULLET_SHOOT_SOUND.play()
            
            if i.type == PLAYER_ONE_HIT:
                global PLAYER_ONE_HEALTH
                PLAYER_ONE_HEALTH -= 1
                BULLET_HIT_SOUND.play()

            if i.type == PLAYER_TWO_HIT:
                global PLAYER_TWO_HEALTH
                PLAYER_TWO_HEALTH -= 1
                BULLET_HIT_SOUND.play()
            
        result = ""
        if PLAYER_ONE_HEALTH <= 0:
            result = "player two!"

        if PLAYER_TWO_HEALTH <= 0:
            result = "player one!"

        if result != "":
            draw_winner(result)
            break

        #print(player_one_bullets, player_two_bullets)
        keys_pressed = pygame.key.get_pressed()
        handle_movement_one(keys_pressed, player_one)
        handle_movement_two(keys_pressed, player_two)

        handle_bullets(player_one_bullets, player_two_bullets, player_one, player_two)

        draw_window(player_one, player_two, player_one_bullets, player_two_bullets, PLAYER_ONE_HEALTH, PLAYER_TWO_HEALTH)


    pygame.quit()
if __name__ == "__main__":
    main()
