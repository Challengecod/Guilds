import pygame
from halfsuper import HSuper
from nosuper import NSuper
from fullsuper import FSuper
from cookies import Cookie
from coin import Coin
import random
from blocks import Block
from ice import ICEA
from square import Squares

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 18)
my_second_font = pygame.font.SysFont('Arial', 30)
cj = pygame.image.load("cookie_jump.png")
cj_two = pygame.transform.scale(cj, (90, 100))
pygame.display.set_caption("Cookie Dogde")
bg = pygame.image.load("ice bg.png")
bg = pygame.transform.scale(bg, (810, 600))
g_bg = pygame.image.load("background.png")



# set up variables for the display
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

#colours
colours = ["crimson", "chartreuse", "coral", "darkorange", "forestgreen", "lime", "navy"]

r = 255
g = 255
b = 255

f = Cookie(50,50)
hs = HSuper(600,480)
ns = NSuper(600,500)
fs = FSuper(600,470)
c = Coin(500, random.randint(0,500))
bl = Block(800, random.randint(0,500))
ic = ICEA(800, random.randint(0,500))

score = 0
super = ns
click = False
change_bg = False
stun = False
point = 0
game_over = False
next_level = False
new_level = 0
level = 1
jump = False
square_pass = 0
win = False

#create sprite group for squares
squares = pygame.sprite.Group()

#create square and add to squares group
square = Squares("crimson", 500, 300)
# squares.add(square)

# render the text for later
start_clicking = my_font.render("START CLICKING ON THE SCREEN! ", True, (0,0,0))
game_over_display = my_second_font.render("GAME OVER! ", True, (255,0,0))
display_win = my_second_font.render("WIN! ", True, (0,255,0))
point_display = my_font.render("Points:" + str(point), True, (0,0,0))
display_lose = my_second_font.render("You've touched the squares!", True, (255,0,0))
display_level = my_font.render("Level:" + str(level), True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
while run:

    if next_level is True:
        if new_level == 10 and level == 1:
            level = 2
            display_level = my_font.render("Level:" + str(level), True, (255, 255, 255))
            new_level = 0

        elif new_level == 20:
            level = 3
            display_level = my_font.render("Level:" + str(level), True, (255, 255, 255))

        if level == 3 and new_level == 60:
            win = True
            change_win_bg = True


    if stun == False:
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            f.move_direction("right", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_a]:
            f.move_direction("left", SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_SPACE]:
            jump = True
            f.move_cookie("up")

        elif not keys[pygame.K_SPACE]:
            f.move_cookie("down")

    elif stun == True:
        game_over = True

    c.move_coin()
    bl.move_block()
    ic.move_ice()

    if int(c.x) == 0:
        c.set_location(800,random.randint(0,590))

    if int(bl.x) == 0:
        bl.set_location(800,random.randint(0,590))

    if int(ic.x) == 0:
        ic.set_location(800,random.randint(0,590))

    if int(f.x) == 0:
        game_over = True

    if f.rect.colliderect(c.rect):
        point += 10
        point_display = my_font.render("Points:" + str(point), True, (0, 0, 0))
        c.set_location(0, random.randint(0, 600))
        score += 1
        if score == 1:
            super = hs
        if score == 2:
            super = fs

    if f.rect.colliderect(bl.rect):
        stun = True

    if f.rect.colliderect(ic.rect):
        change_bg = True

    for square in squares.sprites():
        if f.rect.colliderect(square.rect):
            game_over = True
            print("crash")

        elif square.y >= 600:
            next_level = True
            new_level += 1
            print(new_level)

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if super == fs and event.type == pygame.MOUSEBUTTONDOWN:
            if super.rect.collidepoint(event.pos):
                click = True
                super = ns
                score = 0

                if level == 1:
                    for i in range(5):
                        square = Squares(random.choice(colours), random.randint(0, 800), random.randint(0, 50))
                        squares.add(square)

                elif level == 2:
                    for i in range(10):
                        square = Squares(random.choice(colours), random.randint(0, 800), random.randint(0, 70))
                        squares.add(square)

                elif level == 3:
                    for i in range(20):
                        square = Squares(random.choice(colours), random.randint(0, 800), random.randint(0, 90))
                        squares.add(square)


        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    # draw sprite group


    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##


    if win is True:
        screen.blit(display_win, (250, 290))

    elif game_over is True:
        screen.blit(game_over_display, (250,290))
        screen.blit(display_lose, (270, 330))

    elif game_over is False or win is False:
        if change_bg == True:
            screen.blit(bg, (-5, 0))

        else:
            screen.blit(g_bg, (0, 0))
            screen.blit(ic.image, ic.rect)

        if jump is True:
            screen.blit(cj_two, (f.x, f.y))
            jump = False

        else:
            screen.blit(f.image, f.rect)

        screen.blit(super.image, super.rect)
        screen.blit(super.image, super.rect)
        screen.blit(super.image, super.rect)
        screen.blit(c.image, c.rect)
        screen.blit(bl.image, bl.rect)
        screen.blit(point_display, (50, 50))
        screen.blit(display_level, (70, 70))

        squares.draw(screen)
        squares.update()


    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()