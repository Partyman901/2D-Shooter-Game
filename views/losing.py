import pygame

class LosingScreen:
    def show(self, window, score):
        """ Displays losing screen if player dies """
        font1 = pygame.font.SysFont("arial", 72, bold=True)
        font2 = pygame.font.SysFont("arial", 42, bold=True)
        text1 = font1.render("Game Over!", True, (0,0,0))
        text2 = font2.render(f"Your score is: {score}", True, (0,0,0))
        window.fill((255,255,255))
        window.blit(text1, (195, 100))
        window.blit(text2, (235, 250))
        pygame.display.flip()
