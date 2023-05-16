import pygame
import random

pygame.init()

win_width, win_height = 400, 400

win_display = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("snake game 2.0")

class snake: #note: 
    def __init__(self, snake_x, snake_y):
        self.pos_x = snake_x
        self.pos_y = snake_y
        self.body_list = [(self.pos_x, self.pos_y)]
        self.displace_x = 10
        self.displace_y = 0
    def update(self, diff_x, diff_y):
        pass
    def move_snake():
        pass


base_width, base_height = 10, 10

snake_one_pos_x, snake_one_pos_y = 200, 200
snake_is_dead = False
body_list_one = [(snake_one_pos_x, snake_one_pos_y)]
displace_one_x, displace_one_y = 10, 0

food_pos_x, food_pos_y = random.randrange(0, win_width) // 10 * 10, random.randrange(0, win_height) // 10 * 10

COLOR = {
    "white" : (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0)
}

font = pygame.font.SysFont("bahnschrift", 25) 


clock = pygame.time.Clock()

def snake_one():
    global snake_one_pos_x, snake_one_pos_y, food_pos_x, food_pos_y, snake_is_dead
    snake_one_pos_x = (snake_one_pos_x + displace_one_x) % win_width
    snake_one_pos_y = (snake_one_pos_y + displace_one_y) % win_height

    if((snake_one_pos_x, snake_one_pos_y) in body_list_one):
        snake_is_dead = True
        return

    body_list_one.append((snake_one_pos_x, snake_one_pos_y))
    
    if (food_pos_x == snake_one_pos_x and food_pos_y == snake_one_pos_y):
        while((food_pos_x, food_pos_y) in body_list_one):
            food_pos_x, food_pos_y = random.randrange(0, win_width) // 10 * 10, random.randrange(0, win_height) // 10 * 10
    else:
        del body_list_one[0] #elements will constantly appent to bodylist, however, the last added element will always be removed if the location of the snake does not match with the food location
    
    win_display.fill(COLOR["black"])
    score_count = font.render("score: " + str(len(body_list_one)), True, COLOR["white"])
    win_display.blit(score_count, [0, 0])
    pygame.draw.rect(win_display, (COLOR["red"]), [food_pos_x, food_pos_y, base_width, base_height])
    for (i,j) in body_list_one:
        pygame.draw.rect(win_display, (COLOR["white"]), [i, j, base_width, base_height])
    pygame.display.update()


while True: 
    if snake_is_dead:
        win_display.fill(COLOR["black"])
        score_count = font.render("score: " + str(len(body_list_one)), True, COLOR["white"])
        win_display.blit(score_count, [0, 0])

        lose_msg = font.render("GAME OVER", True, COLOR["white"])
        win_display.blit(lose_msg, [win_width // 3, win_height // 3])
        pygame.display.update()
        pygame.time.delay(2000)

        pygame.quit()
        quit()

    events = pygame.event.get()
    for i in events:
        if (i.type == pygame.QUIT):
            pygame.quit()
            quit()
        if(i.type == pygame.KEYDOWN):
            match i.key:
                case pygame.K_LEFT:
                    if displace_one_x != 10:
                        displace_one_x = -10
                    displace_one_y = 0

                case pygame.K_RIGHT:
                    if displace_one_x != -10:
                        displace_one_x = 10
                    displace_one_y = 0

                case pygame.K_UP:
                    displace_one_x = 0
                    if displace_one_y != 10:
                        displace_one_y = -10

                case pygame.K_DOWN:
                    displace_one_x = 0
                    if displace_one_y != -10:
                        displace_one_y = 10
                case _:
                    continue
            snake_one()
    if (not events):
        snake_one()

    clock.tick(10)




"""
check inputs and update them globally (snake positions)
with or without input, call snake() function

constantly update snake position
check if current snake position is in the body list (previous snake positions), if true, kill the snake, if false, continue through code
append the current snake position in into the body list
check if current snake position is the same as the red dot's position, if yes, keep updating the red dot's position while it's location continues to match with any elements. 
    if no, just delete the last added element in the body list
fill the background with blit function (black background)
render score count text
render the red dot AKA food
render every location in body list by interrating with (i,j) with rect
update the display

"""