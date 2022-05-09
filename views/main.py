import pygame

class MainView:
    """ Main display and update for the game """
    def __init__(self, window):
        self.window = window
        self.farm_bg = pygame.image.load('assets/farmbg/farm.png')

    def draw_game_window(self, player, airdramons, fireballs, font, score):
        """ Updates the game window """
        self.window.blit(self.farm_bg, (0,0))
        text = font.render('Score: ' + str(score), 1, (0,0,0))
        self.window.blit(text, (5, 10))
        player.draw(self.window)
        for fire in fireballs:
            fire.draw(self.window)
        for mon in airdramons:
            mon.draw(self.window)
        pygame.display.update()