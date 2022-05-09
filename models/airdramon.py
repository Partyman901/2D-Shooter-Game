import pygame
import pygame.locals
import random

class Airdramon(pygame.sprite.Sprite):
    """ Creates enemy Airdramon to attack the player """
    def __init__(self):
        super().__init__()
        self.fly = [pygame.image.load('assets/airdramon/airdramon1.png'),
            pygame.image.load('assets/airdramon/airdramon2.png'),
            pygame.image.load('assets/airdramon/airdramon3.png'),
            pygame.image.load('assets/airdramon/airdramon4.png')]
        self.rect = self.fly[0].get_rect()
        self.rect.y = random.randint(50, 400)
        self.rect.x = 750
        self.vel = 6
        self.flyCount = 0
        self.width = 150
        self.height = 150
        self.mask = pygame.mask.from_surface(pygame.transform.scale(self.fly[0], (self.width, self.height)).convert_alpha())
        self.health = 70
        self.dead = False

    def draw(self, win):
        """ Draws Airdramon animation onto a surface """
        if self.flyCount + 1 > 36:
            self.flyCount = 0
        win.blit(pygame.transform.scale(self.fly[self.flyCount//9],(self.width, self.height)), (self.rect.x, self.rect.y))
        self.flyCount += 1
        pygame.draw.rect(win, (0,0,0), (self.rect.x + 17, self.rect.y - 12, 75, 15))
        pygame.draw.rect(win, (255,0,0), (self.rect.x + 20, self.rect.y - 10, 70, 10))
        pygame.draw.rect(win, (0,255,0), (self.rect.x + 20, self.rect.y - 10, self.health, 10))

    def update(self, airdramons):
        """ Moves and spawns instances of Airdramon """
        self.rect.x -= self.vel

        if (self.rect.x < 500 and len(airdramons) < 3):
            airdramons.add(self.__class__())
        if self.rect.x <= 0:
            self.kill()
        
    def damaged(self):
        """ Damages enemy, if health reaches 0, enemy dies """
        if self.health > 0:
            self.health -= 10
        else:
            self.dead = True