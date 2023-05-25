import pygame
import random

pygame.init()

# i love classes now.

win_width, win_height = 400, 400

win_display = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("snake game 2.0")


def end_game(result):
    match result:
        case "win":
            fill_background()
            show_score()
            show_win_message()
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            quit()

        case "lose":
            fill_background()
            show_score()
            show_lose_message()

            pygame.display.update()
            pygame.time.delay(2000)

            pygame.quit()
            quit()

base_width, base_height = 10, 10
give_length = [True, True]

def get_num_within_range(axis):
    num = 0
    match axis:
        case "x":
            num = random.randrange(0, win_width) // 10 * 10
        case "y":
            num = random.randrange(0, win_height) // 10 * 10
    return num

def fill_background():
    win_display.fill(COLOR["black"])

def show_score():
    score_count = font.render("score: " + str(len(snake1.body_list)), True, COLOR["white"])
    win_display.blit(score_count, [0, 0])

def show_lose_message():
    lose_msg = font.render("GAME OVER", True, COLOR["white"])
    win_display.blit(lose_msg,  [win_width // 3, win_height // 3])

def show_win_message():
    win_msg = font.render("YOU WIN!", True, COLOR["white"])
    win_display.blit(win_msg,  [win_width // 3, win_height // 3])

class food:
    def __init__(self, food_x, food_y):
        self.pos_x = food_x
        self.pos_y = food_y
    def reset_position(self, eaten_by):
        self.pos_x, self.pos_y = get_num_within_range("x"), get_num_within_range("y")
        global game_end
        match eaten_by:
            case "AI":
                try: 
                    del snake1.body_list[0]
                except:
                    end_game("lose")
            case "PLAYER":
                try: 
                    if len(snake2.body_list) > 1:
                        del snake2.body_list[0]
                    else:
                        end_game("win")
                        #snake2.body_list = []

                except:
                    pygame.quit()
                    quit()
                    #end_game("win")
                    
    def draw_food(self):
        global base_width, base_height
        pygame.draw.rect(win_display, (COLOR["red"]), [self.pos_x, self.pos_y, base_width, base_height])

class snake: #note: 
    def __init__(self, snake_x, snake_y):
        self.pos_x = snake_x
        self.pos_y = snake_y
        self.displace_x = 10
        self.displace_y = 0
        self.body_list = [(self.pos_x, self.pos_y)]
        self.last_turned = 0
        self.last_displace = "y"
    def pick_direction(self, target_x, target_y):
        if target_x == self.pos_x:
            self.displace_x = 0
            if target_y > self.pos_y:
                self.displace_y = 10
            elif target_y < self.pos_y:
                self.displace_y = -10
        elif target_y == self.pos_y:
            self.displace_y = 0
            if target_x > self.pos_x:
                self.displace_x = 10
            elif target_x < self.pos_x:
                self.displace_x = -10
        elif target_x > self.pos_x:
            self.displace_x = 10
        elif target_x < self.pos_x:
            self.displace_x = -10
        else:
            self.displace_x = 10
            self.displace_y = 0
    def remove_newest_element(self):
        del self.body_list[0]

    def handle_snake(self, target_x, target_y, snake_type):
        global game_end
        show_score()
        match snake_type:
            case "AI":
                if give_length[1]:
                    self.element = self.pos_x
                    for i in range(2):
                        self.body_list.append((self.element - 1, self.pos_y))
                        self.element = self.element - 1
                give_length[1] = False

                self.pick_direction(target_x, target_y)
                if random.choice([True, False, False, False]):
                    if self.displace_x != 0:
                        self.pos_x = (self.pos_x + self.displace_x) % win_width
                    else:
                        self.pos_y = (self.pos_y + self.displace_y) % win_height
                else:
                    self.pos_x = (self.pos_x + self.displace_x) % win_width
                    self.pos_y = (self.pos_y + self.displace_y) % win_height
                self.body_list.append((self.pos_x, self.pos_y))
                if (target_x == self.pos_x and target_y == self.pos_y):
                    red_dot.reset_position("AI")
                else:
                    self.remove_newest_element()
                red_dot.draw_food()
                for (i,j) in self.body_list:
                    try: 
                        if (i,j) != snake1.body_list[-1]:
                            pygame.draw.rect(win_display, (COLOR["white"]), [i, j, base_width, base_height])
                        else:
                            pygame.draw.rect(win_display, (COLOR["orange"]), [i, j, base_width, base_height])
                    except:
                        end_game("lose")
                pygame.display.update()
            case "PLAYER":
                if give_length[0]:
                    self.element = self.pos_x
                    for i in range(5):
                        self.body_list.append((self.element - 1, self.pos_y))
                        self.element = self.element - 1
                give_length[0] = False

                self.pos_x = (self.pos_x + self.displace_x) % win_width
                self.pos_y = (self.pos_y + self.displace_y) % win_height
                self.body_list.append((self.pos_x, self.pos_y))

                if (target_x == self.pos_x and target_y == self.pos_y):
                    red_dot.reset_position("PLAYER")
                else:
                    self.remove_newest_element()
                show_score()
                for (i,j) in self.body_list:
                    try: 
                        pygame.draw.rect(win_display, (COLOR["yellow"]), [i, j, base_width, base_height])
                    except:
                        end_game("win")
                pygame.display.update()
                red_dot.draw_food()
            case _:
                pass
                # elements will constantly appent to bodylist, however, the last added element will always be 
                # removed if the location of the snake does not match with the food location


COLOR = {
    "white" : (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "yellow": (255, 255, 0),
    "orange": (255, 127, 0)
}

font = pygame.font.SysFont("bahnschrift", 25) 

snake1 = snake(get_num_within_range("x"), get_num_within_range("y"))
snake2 = snake(get_num_within_range("x"), get_num_within_range("y"))
red_dot = food(get_num_within_range("x"), get_num_within_range("y"))
clock = pygame.time.Clock()

def get_keys():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake1.displace_x = -10
        if keys[pygame.K_UP]:
            snake1.displace_y = -10
        elif keys[pygame.K_DOWN]:
            snake1.displace_y = 10
        else:
            snake1.displace_y = 0
    elif keys[pygame.K_RIGHT]:
        snake1.displace_x = 10
        if keys[pygame.K_UP]:
            snake1.displace_y = -10
        elif keys[pygame.K_DOWN]:
            snake1.displace_y = 10
        else:
            snake1.displace_y = 0
    elif keys[pygame.K_UP]:
        snake1.displace_y = -10
        if keys[pygame.K_LEFT]:
            snake1.displace_x = -10
        elif keys[pygame.K_RIGHT]:
            snake1.displace_x = 10
        else:
            snake1.displace_x = 0
    elif keys[pygame.K_DOWN]:
        snake1.displace_y = 10
        if keys[pygame.K_LEFT]:
            snake1.displace_x = -10
        elif keys[pygame.K_RIGHT]:
            snake1.displace_x = 10
        else:
            snake1.displace_x = 0



def main():
    while True:
        for i in pygame.event.get():
            if (i.type == pygame.QUIT):
                pygame.quit()
                quit()
        get_keys()
        fill_background()
        snake1.handle_snake(red_dot.pos_x, red_dot.pos_y, "PLAYER")
        snake2.handle_snake(red_dot.pos_x, red_dot.pos_y, "AI")
        clock.tick(10)
if __name__ == "__main__":
    main()


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
