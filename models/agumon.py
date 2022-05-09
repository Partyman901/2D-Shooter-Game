import pygame
import pygame.locals

class Agumon(pygame.sprite.Sprite):
    """ Creates an Agumon for the player to control """
    def __init__(self, x, y, width, height):
        super().__init__()
        self.move = [pygame.image.load('assets/agumon/agumon1.png'), 
            pygame.image.load('assets/agumon/agumon2.png'),
            pygame.image.load('assets/agumon/agumon3.png'),
            pygame.image.load('assets/agumon/agumon4.png'),
            pygame.image.load('assets/agumon/agumon5.png'),
            pygame.image.load('assets/agumon/agumon6.png'),
            pygame.image.load('assets/agumon/agumon7.png'),
            pygame.image.load('assets/agumon/agumon8.png'),
            pygame.image.load('assets/agumon/agumon9.png'),
            pygame.image.load('assets/agumon/agumon10.png'),
            pygame.image.load('assets/agumon/agumon11.png'),
            pygame.image.load('assets/agumon/agumon12.png')]
        self.health = 70
        self.rect = self.move[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.walkCount = 0
        self.fire_timer = 0
        self.fire_rate = 10
        self.special = False
        self.special_timer = 70
        self.isalive = True
        self.mask = pygame.mask.from_surface(pygame.transform.scale(self.move[0], (self.width, self.height)).convert_alpha())

    def draw(self, win):
        """ Draws player animation """
        if self.walkCount + 1 > 36:
            self.walkCount = 0
        win.blit(pygame.transform.scale(self.move[self.walkCount//3], (self.width, self.height)), (self.rect.x, self.rect.y))
        self.walkCount += 1
        pygame.draw.rect(win, (0,0,0), (self.rect.x - 3, self.rect.y - 20, 75, 22))
        pygame.draw.rect(win, (255,0,0), (self.rect.x, self.rect.y - 10, 70, 10))
        pygame.draw.rect(win, (0,255,0), (self.rect.x, self.rect.y - 10, self.health, 10))
        pygame.draw.rect(win, (50,50,255), (self.rect.x, self.rect.y - 17, self.special_timer, 7))

    def special_setter(self):
        """ If special meter is full, unlimits projectile spacing. Finishes when meter is done """
        if self.special == True: # If player is using special, 
                self.fire_rate = 1
                self.special_timer -= 0.5
                if self.special_timer <= 0:
                    self.special = False
                    self.fire_rate = 7