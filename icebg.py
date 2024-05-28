import pygame


class Icebg:

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
        scale_size = (self.image_size[0] * .9, self.image_size[1] * .9)
        self.image = pygame.transform.scale(self.image, scale_size)




