import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display size
width = 600
height = 400

# Set display
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Snake block and speed
block_size = 10
snake_speed = 15

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    win.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    # Starting position
    x1 = width / 2
    y1 = height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(blue)
            message("You lost! Press C to play again or Q to quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Borders
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(blue)

        # Draw food
        pygame.draw.rect(win, green, [foodx, foody, block_size, block_size])

        # Update snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Collision with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(block_size, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Food eaten
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


def draw_snake(block_size, snake_list):
    for i, x in enumerate(snake_list):
        if i == len(snake_list) - 1:
            # Snake head
            pygame.draw.rect(win, (0, 100, 0), [x[0], x[1], block_size, block_size])

            # Eyes
            eye_radius = 2
            eye_offset_x = 2
            eye_offset_y = 2
            pygame.draw.circle(win, white, (int(x[0] + eye_offset_x), int(x[1] + eye_offset_y)), eye_radius)
            pygame.draw.circle(win, white, (int(x[0] + block_size - eye_offset_x * 2), int(x[1] + eye_offset_y)),
                               eye_radius)
        else:
            # Body
            pygame.draw.rect(win, black, [x[0], x[1], block_size, block_size])
import pygame
import time
import random

# Initialize
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display size
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with Levels & Music")

# Clock
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load music
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)  # Loop forever

# Optional: Eating sound
# eat_sound = pygame.mixer.Sound("eat.wav")

block_size = 10

def your_score(score, level):
    value = score_font.render(f"Score: {score}   Level: {level}", True, yellow)
    win.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for i, x in enumerate(snake_list):
        if i == len(snake_list) - 1:
            # Head with eyes
            pygame.draw.rect(win, (0, 100, 0), [x[0], x[1], block_size, block_size])
            eye_radius = 2
            pygame.draw.circle(win, white, (int(x[0] + 2), int(x[1] + 2)), eye_radius)
            pygame.draw.circle(win, white, (int(x[0] + block_size - 4), int(x[1] + 2)), eye_radius)
        else:
            pygame.draw.rect(win, black, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    score = 0
    level = 1
    snake_speed = 15

    while not game_over:

        while game_close:
            win.fill(blue)
            message("You lost! Press C to play again or Q to quit", red)
            your_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(blue)

        pygame.draw.rect(win, green, [foodx, foody, block_size, block_size])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(block_size, snake_List)
        your_score(score, level)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1
            # eat_sound.play()

            # Level up every 5 points
            if score % 5 == 0:
                level += 1
                snake_speed += 3

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

# Start game
gameLoop()
