import pygame
from halfsuper import HSuper
from nosuper import NSuper
from fullsuper import FSuper
from fox import Fox
from coin import Coin
import random
# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("")

# set up variables for the display
SCREEN_HEIGHT = 780
SCREEN_WIDTH = 1300
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

r = 255
g = 255
b = 255

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
f = Fox(50,50)
hs = HSuper(1100,600)
ns = NSuper(1100,600)
fs = FSuper(1100,600)
c = Coin(random.randint(0,1300), random.randint(0,780))
score = 0
super = ns


# -------- Main Program Loop -----------
while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        f.move_direction("right", SCREEN_WIDTH, SCREEN_HEIGHT)

    if keys[pygame.K_a]:
        f.move_direction("left", SCREEN_WIDTH, SCREEN_HEIGHT)

    if keys[pygame.K_w]:
        f.move_direction("up", SCREEN_WIDTH, SCREEN_HEIGHT)

    if keys[pygame.K_s]:
        f.move_direction("down", SCREEN_WIDTH, SCREEN_HEIGHT)

    if f.rect.colliderect(c.rect):
        score += 1
        if score == 1:
            super = hs
        if score == 2:
            super = fs

        c.set_location(random.randint(50, 1300), random.randint(50, 780))

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and super == fs:
            if super.rect.collidepoint(event.pos):
                super = ns
                score = 0


    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    screen.fill((r, g, b))
    screen.blit(super.image, super.rect)
    screen.blit(super.image, super.rect)
    screen.blit(super.image, super.rect)
    screen.blit(f.image, f.rect)
    screen.blit(c.image, c.rect)


    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()