import pygame
from halfsuper import HSuper
from nosuper import NSuper
from fullsuper import FSuper
from fox import Fox
from coin import Coin
import random
from blocks import Block
from ice import ICEA
from icebg import Icebg
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
bg = pygame.image.load("ice bg.PNG")
f = Fox(50,50)
hs = HSuper(1100,600)
ns = NSuper(1100,600)
fs = FSuper(1100,600)
c = Coin(random.randint(0,100), random.randint(0,100))
bl = Block(random.randint(0,1200), random.randint(0,600))
ic = ICEA(random.randint(0,1200), random.randint(0,600))
ibg = Icebg(0,0)
score = 0
super = ns
click = False
change_bg = False

# -------- Main Program Loop -----------
while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        f.move_direction("right", SCREEN_WIDTH, SCREEN_HEIGHT)

    if keys[pygame.K_a]:
        f.move_direction("left", SCREEN_WIDTH, SCREEN_HEIGHT)

    if keys[pygame.K_SPACE]:
        f.move_balloon("up")

    elif not keys[pygame.K_SPACE]:
        f.move_balloon("down")
    c.move_coin()
    bl.move_block()
    ic.move_ice()
    print(c.y)
    if int(c.y) == SCREEN_HEIGHT:
        c.set_location(random.randint(0,1280), 0)
    if int(bl.y) == SCREEN_HEIGHT:
        bl.set_location(random.randint(0,1280), 0)

    if int(ic.y) == SCREEN_HEIGHT:
        ic.set_location(random.randint(0,1280), 0)

    if f.rect.colliderect(c.rect):
        c.set_location(random.randint(0, 1280), 0)
        score += 1
        if score == 1:
            super = hs
        if score == 2:
            super = fs
    if f.rect.colliderect(ic.rect):
        change_bg = True

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and super == fs:
            if super.rect.collidepoint(event.pos):
                click = True
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
    screen.blit(bl.image, bl.rect)
    screen.blit(ic.image, ic.rect)
    if change_bg == True:
        screen.blit(ibg, (0, 0))


    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()