import pygame


class Coin:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("coin-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def move_coin(self):
        # move the balloon up or down based on the direction!
        # don't let the balloon move if it's at the bottom or top of the screen
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.y += 0.2

