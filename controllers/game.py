import pygame
import pygame.locals
import random
import requests
from models import Agumon, Airdramon, Fireball
from views import MainView, LosingScreen

class GameController:
    def __init__(self):
        pygame.display.set_caption("My Game")

        self._win = pygame.display.set_mode((750, 500))
        self.clock = pygame.time.Clock()
        self.player = Agumon(100, 250, 64, 64)

    def run(self):
        """ Main loop that runs the game. Ends if player dies """
        # player = Agumon(100, 250, 64, 64)
        main_view = MainView(self._win)
        pygame.init()
        pygame.display.set_caption("My Game")
        run = True
        airdramons = pygame.sprite.Group()
        airdramons.add(Airdramon())
        fireballs = pygame.sprite.Group()
        clock = pygame.time.Clock()
        score = 0
        font = pygame.font.SysFont('comicsans', 30, True)
        API_URL = "http://localhost:5000/api"
        while run:
            clock.tick(36)

            self.player.special_setter()

            if self.player.health <= 0: # Player dies if they run out of health
                self.player.isalive = False

            if self.player.fire_timer < 0 and self.player.special == False: # Spaces out shots so player is unable to spam fireballs, unless their special is active
                self.player.fire_timer == 0
            elif self.player.fire_timer > 0:
                self.player.fire_timer -= 1

            if len(airdramons) == 0:
                airdramons.add(Airdramon()) # If there's no enemies, spawn more

            for event in pygame.event.get(): # Quits game if game is exited. Saves score if player is dead
                if event.type == pygame.QUIT:
                    if self.player.isalive == False:
                        req = requests.put(f"{API_URL}/score", json={"score": str(score)})
                    run = False
            
            for fire in fireballs:
                if fire.rect.x < 750: # Deletes fireballs when they reach the end of the screen
                    fire.rect.x += fire.vel 
                else:
                    fire.kill()
                            
            for mon in airdramons: # Deletes enemy if they reach the left side of the screen.
                mon.update(airdramons)
                if mon.rect.x <= 0:
                    mon.kill()
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.player.rect.x > 5:
                self.player.rect.x -= self.player.vel
            if keys[pygame.K_RIGHT] and self.player.rect.x < 750 - self.player.width - 5:
                self.player.rect.x += self.player.vel
            if keys[pygame.K_UP] and self.player.rect.y > 5:
                self.player.rect.y -= self.player.vel
            if keys[pygame.K_DOWN] and self.player.rect.y < 500 - self.player.height - 5:       
                self.player.rect.y += self.player.vel
            if keys[pygame.K_SPACE] and self.player.isalive == True: # Fire fireballs if player is alive
                if self.player.fire_timer == 0:
                    fireballs.add(Fireball((round(self.player.rect.x + self.player.width // 2) - 50), round((self.player.rect.y + self.player.height // 2) - 80)))
                    self.player.fire_timer = self.player.fire_rate
            if keys[pygame.K_TAB]: # Activates special
                if self.player.special_timer >= 70:
                    self.player.special = True

            if pygame.sprite.spritecollide(self.player, airdramons, True, pygame.sprite.collide_mask):
                self.player.health -= 10

            hit_airdramons = pygame.sprite.groupcollide(airdramons, fireballs, False, True, collided = pygame.sprite.collide_mask)
            for mon in hit_airdramons:
                mon.damaged()
                if mon.dead == True: # Damages enemy when fireball hits
                    mon.kill()
                    score += 50
                    if self.player.special_timer < 70:
                        self.player.special_timer += 10
                else:
                    score += 1

            if self.player.isalive == True: 
                main_view.draw_game_window(self.player, airdramons, fireballs, font, score)
            else:
                screen = LosingScreen()
                screen.show(self._win, score)

    pygame.quit

