import pygame

class Cookie:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("cookie.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .7
        self.current_direction = "right"

    def rescale_image(self, image):
        self.image_size = self.image.get_size()  # get the image size
        # multiplying the width and height above 0.5 makes the image larger
        scale_size = (self.image_size[0] * .45, self.image_size[1] * .45)
        self.image = pygame.transform.scale(self.image, scale_size)  # transforming to your scale

    def move_cookie(self, direction):
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.x += 1

        if self.y >= 0 and self.y < 600:
            if direction == 'up':
                self.y -= 2
            else:
                self.y += 2


    def move_direction(self, direction, screen_width, screen_height):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)

        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)

        if direction == "left":
            self.current_direction = "left"
            if self.x - self.delta >= 0 :  # copy this to all the other directions (MAKE SURE ITS THE CORRECT BORDER)
                self.x -= 3

        if direction == "up":
            self.current_direction = "up"
            if self.y - self.delta >= 0:  # copy this to all the other directions (MAKE SURE ITS THE CORRECT BORDER)
                self.y -= self.delta

        if direction == "down":
            self.current_direction = "down"
            if self.y + self.delta <= 600:  # copy this to all the other directions (MAKE SURE ITS THE CORRECT BORDER)
                self.y += self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])




