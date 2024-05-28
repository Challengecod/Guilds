import pygame


class ICEA:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("ice age.PNG")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
        self.image = pygame.transform.scale(self.image, scale_size)

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def move_ice(self):
        # move the balloon up or down based on the direction!
        # don't let the balloon move if it's at the bottom or top of the screen
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.y += 0.2
