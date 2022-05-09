import pygame

class Fireball(pygame.sprite.Sprite):
    """ Creates a fire projectile instance """
    def __init__(self, x, y):
        super().__init__()
        self.image = [pygame.image.load('assets/fireball/fire1.png'),
            pygame.image.load('assets/fireball/fire2.png'),
            pygame.image.load('assets/fireball/fire3.png'),
            pygame.image.load('assets/fireball/fire4.png'),
            pygame.image.load('assets/fireball/fire5.png'),
            pygame.image.load('assets/fireball/fire6.png')]
        self.rect = self.image[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 15
        self.fireCount = 0
        self.width = 30
        self.height = 30
        self.mask = pygame.mask.from_surface(self.image[0].convert_alpha())

    def draw(self, win):
        """ Draws fireball animation to a surface """
        if self.fireCount + 1 > 36:
            self.fireCount = 0
        win.blit(self.image[self.fireCount//6], (self.rect.x, self.rect.y))
        self.fireCount += 1
