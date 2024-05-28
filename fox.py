import pygame

class Fox:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("orange-fox-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .7
        self.current_direction = "right"

    def move_balloon(self, direction):
        # move the balloon up or down based on the direction!
        # don't let the balloon move if it's at the bottom or top of the screen
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if self.y >= 0 and self.y < 780:
            if direction == 'up':
                self.y -= 1
            else:
                self.y += 1
        elif self.y <= 0:
            self.y = 0
        elif self.y <= 780:
            self.y = 780


    def move_direction(self, direction, screen_width, screen_height):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)

        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)

        if direction == "right":
            self.current_direction = "right"
            if self.x + self.delta <= 1380: # copy this to all the other directions (MAKE SURE ITS THE CORRECT BORDER)
                self.x += self.delta

        if direction == "left":
            self.current_direction = "left"
            if self.x - self.delta >= 0 :  # copy this to all the other directions (MAKE SURE ITS THE CORRECT BORDER)
                self.x -= self.delta

        if direction == "up":
            self.current_direction = "up"
            if self.y - self.delta >= 0:  # copy this to all the other directions (MAKE SURE ITS THE CORRECT BORDER)
                self.y -= self.delta

        if direction == "down":
            self.current_direction = "down"
            if self.y + self.delta <= 780:  # copy this to all the other directions (MAKE SURE ITS THE CORRECT BORDER)
                self.y += self.delta


        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

