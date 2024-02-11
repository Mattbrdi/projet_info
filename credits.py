import pygame
from button import Button
import sys

class Credits:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.SysFont("Georgia", 40)
        self.background = pygame.image.load("images/main_menu.png")
        self.text_lines = [
            "Bravo vous avez réussi!",
            "Par Mattis BORDERIES",
            "Amine AMZAI",
            "Maxime de BUSSAC",
            "Raphael POUX"
        ]
        self.text_surfaces = [self.font.render(line, True, (255, 0, 0)) for line in self.text_lines]
        self.text_rects = [surface.get_rect(center=(400, 200 + i * 30)) for i, surface in enumerate(self.text_surfaces)]
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
                        self.screen.fill((0, 0, 0))
                        return 
            self.screen.blit(self.background, (70, 70))
            for surface, rect in zip(self.text_surfaces, self.text_rects):
                self.screen.blit(surface, rect)
            self.back_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()