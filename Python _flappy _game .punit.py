import pygame
import random
import sys

bif="bg.jpg"
mif = "images.png"

# Initialising the modules in pygame
pygame.init()

SCREEN = pygame.display.set_mode((500, 750))  # Setting the display

# background
BACKGROUND_IMAGE = pygame.image.load('punit.png.png')

#  BIRD
BIRD_IMAGE = pygame.image.load('punit.bird.png')
Bird_x = 50
Bird_y = 300
Bird_y_change = 0

def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))

# OBSTACLES
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (211, 253, 117)
OBSTACE_X_CHANGE = -4
Obstacle_x = 500

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (Obstacle_x, 0, OBSTACLE_WIDTH, height))
    Bottom_obstacle_height = 635-height-150
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (Obstacle_x, 635, OBSTACLE_WIDTH, -bottom_obstacle_height))

# COLLISION DETECTION
def collision_detection (obstacle_x, obstacle_height, Bird_y, Bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if Bird_y <= obstacle_height or Bird_y >= (bottom_obstacle_height - 64):
            return True
    return False

# SCORE
Score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
    SCREEN.blit(display, (10, 10))

# START SCREEN
startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
    # displays: “press space bar to start)
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    SCREEN.blit(display, (20, 200))
    pygame.display.update()

# GAME OVER SCREEN
# This list will hold all of the scores
Score_list = [0]

Game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
Game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

def game_over():
    # check for the maximum score
    Maximum = max(score_list)
    #  “game over”
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    SCREEN.blit(display1, (50, 300))
    # shows your current score and your max score
    Display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (50, 400))
    #  If your new score is the same as the maximum then u reached a new high score
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (200,35,35))
        SCREEN.blit(display3, (80, 100))

Running = True
# waiting is going to refer to our end or start screen
Waiting = True
# set collision to false in the beginning so that we only see the start screen in the beginning
Collision = False

while Running:

    SCREEN.fill((0, 0, 0))

    # display the background image
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    # we will be sent into this while loop at the beginning and ending of each game
    while Waiting:
        if Collision:
        
            # If collision is True (from the second time onwards) we will see both the end screen and the start screen
            Game_over()
            start()
        else:
            # This refers to the first time the player is starting the game
            start()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

            
                    #  If we press the space bar we will exit out of the waiting while loop and start to play the game
                    # we will also reset some of the variables such as the score and the bird’s Y position and the obstacle’s starting position
                    Score = 0 
                    Bird_y = 300
                    Obstacle_x = 500
                    #  to exit out of the while loop
                    Waiting = False

            if event.type == pygame.QUIT:
                # in case we exit out make both running and waiting false
                Waiting = False
                Running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If you press exit you exit out of the while loop and pygame quits
            Running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #  if you press spacebar you will move up
                Bird_y_change = -6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # when u release space bar you will move down automatically
                Bird_y_change = 3

    # moving the bird vertically
    Bird_y += Bird_y_change
    # setting boundaries for the birds movement
    if Bird_y <= 0:
        Bird_y = 0
    if Bird_y >= 571:
        Bird_y = 571

    # Moving the obstacle
    Obstacle_x += OBSTACE_X_CHANGE

    # COLLISION
    Collision = collision_detection(Obstacle_x, OBSTACLE_HEIGHT, Bird_y, OBSTACLE_HEIGHT + 150)

    if Collision:
        # if a collision does occur we are gonna add that score to our list of scores and make waiting True
        Score_list.append(score)
        Waiting = True

    # generating new obstacles
    if Obstacle_x <= -10:
        Obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        Score += 1
    # displaying the obstacle
    display_obstacle(OBSTACLE_HEIGHT)

    # displaying the bird
    display_bird(bird_x, bird_y)

    # display the score
    score_display(score)

    # Update the display after each iteration of the while loop
    pygame.display.update()

# Quit the program
pygame.quit()
