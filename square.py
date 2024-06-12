import pygame

class Squares(pygame.sprite.Sprite):

  def __init__(self, col, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    self.image = pygame.Surface((20, 20))
    self.image.fill(col)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.delta = 5

  def update(self):
    self.rect.move_ip(0,5)
    self.y += 5
    if self.rect.top >= 600:
      self.kill()