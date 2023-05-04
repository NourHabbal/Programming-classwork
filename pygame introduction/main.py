import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("le game") 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 0, 0)
YELLOW = (255, 255, 0)
MOVE_SPEED = 3
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

BORDER = pygame.Rect(WIDTH//2, 0, 10, HEIGHT)
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 80
BULLET_SPEED = 7
BULLET_MAX = 5

PLAYER_ONE_HIT = pygame.USEREVENT + 1
PLAYER_TWO_HIT = pygame.USEREVENT + 2

PLAYER_ONE_HEALTH = 7
PLAYER_TWO_HEALTH = 7

SPRITE_IMAGE1 = pygame.image.load(os.path.join("pygame introduction", "asset", "sprite1.png"))
SPRITE_IMAGE2 = pygame.image.load(os.path.join("pygame introduction", "asset", "sprite2.png"))

SPRITE_EDIT1 = pygame.transform.rotate(pygame.transform.scale(SPRITE_IMAGE1, (PLAYER_WIDTH, PLAYER_HEIGHT)), 180 )
SPRITE_EDIT2 = pygame.transform.rotate(pygame.transform.scale(SPRITE_IMAGE2, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0 )

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("pygame introduction", "asset", "background.png")), (WIDTH, HEIGHT))

def draw_window(one, two, one_bullets, two_bullets, player_health_one, player_health_two):
    #WIN.fill((WHITE))
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(SPRITE_EDIT1, (one.x, one.y))
    WIN.blit(SPRITE_EDIT2, (two.x, two.y))
    player_one_text = HEALTH_FONT.render("HP: " + str(player_health_one), 1, WHITE)
    player_two_text = HEALTH_FONT.render("HP: " + str(player_health_two), 1, WHITE)

    WIN.blit(player_one_text, (WIDTH - player_one_text.get_width() - 10, 10))
    WIN.blit(player_two_text, (10, 10))

    for bullet in one_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in two_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def handle_movement_one(keys_pressed, player_given):
    if keys_pressed[pygame.K_a] and player_given.x - MOVE_SPEED > 0:  # LEFT
        player_given.x -= MOVE_SPEED
    if keys_pressed[pygame.K_d] and player_given.x + MOVE_SPEED + player_given.width < BORDER.x:  # RIGHT
        player_given.x += MOVE_SPEED
    if keys_pressed[pygame.K_w] and player_given.y - MOVE_SPEED > 0:  # UP
        player_given.y -= MOVE_SPEED
    if keys_pressed[pygame.K_s] and player_given.y + MOVE_SPEED + player_given.height < HEIGHT:  # DOWN
        player_given.y += MOVE_SPEED


def handle_movement_two(keys_pressed, player_given):
    if keys_pressed[pygame.K_j] and player_given.x - MOVE_SPEED > BORDER.x + BORDER.width: #LEFT
        player_given.x -= MOVE_SPEED
    if keys_pressed[pygame.K_l] and player_given.x + MOVE_SPEED + player_given.width < WIDTH: #RIGHT
        player_given.x += MOVE_SPEED
    if keys_pressed[pygame.K_i] and player_given.y - MOVE_SPEED > 0: #UP
        player_given.y -= MOVE_SPEED
    if keys_pressed[pygame.K_k] and player_given.y + MOVE_SPEED + player_given.height < HEIGHT: #DOWN
        player_given.y += MOVE_SPEED

def handle_bullets(player_one_bullets, player_two_bullets, player_one, player_two):
    for bullet in player_one_bullets:
        bullet.x += BULLET_SPEED
        if player_two.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER_TWO_HIT))
            player_one_bullets.remove(bullet)
        elif bullet.x > WIDTH: #outside barrier
            player_one_bullets.remove(bullet)

    for bullet in player_two_bullets:
        bullet.x -= BULLET_SPEED
        if player_one.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER_ONE_HIT))
            player_two_bullets.remove(bullet)
        elif bullet.x < 0: #outside barrier
           player_two_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    player_one = pygame.Rect(100, 300,PLAYER_WIDTH, PLAYER_HEIGHT)
    player_two = pygame.Rect(700, 300,PLAYER_WIDTH, PLAYER_HEIGHT)

    player_one_bullets = []
    player_two_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(player_one_bullets) < BULLET_MAX:
                    bullet = pygame.Rect(player_one.x + player_one.width, player_one.y + player_one.height//2 - 2, 10, 5 )
                    player_one_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(player_two_bullets) < BULLET_MAX:
                    bullet = pygame.Rect(player_two.x, player_two.y + player_two.height//2 - 2, 10, 5 )
                    player_two_bullets.append(bullet)
            
            if event.type == PLAYER_ONE_HIT:
                global PLAYER_ONE_HEALTH
                PLAYER_ONE_HEALTH -= 1
            if event.type == PLAYER_TWO_HIT:
                global PLAYER_TWO_HEALTH
                PLAYER_TWO_HEALTH -= 1
            
        result = ""
        if PLAYER_ONE_HEALTH <= 0:
            result = "player two wins"

        if PLAYER_TWO_HEALTH <= 0:
            result = "player two wins"

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

