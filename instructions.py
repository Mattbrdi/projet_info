import pygame
from button import Button
import sys

class Instructions:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.SysFont("Georgia", 20)
        self.background = pygame.image.load("images/main_menu.png")
        self.text = self.font.render("Utiliser les flèches pour se déplacer, ZQSD pour déplacer le portail, TAB pour changer de portail et espace pour lancer un portail", True, (255, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (400, 200)
        self.back_button = Button(60, 500, 200, 50, "Back", font="Georgia")
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.back_button.is_clicked(x, y):
                        return
            self.screen.blit(self.background, (-50, 0))
            self.screen.blit(self.text, self.text_rect)
            self.back_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()