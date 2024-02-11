import pygame

# Creates a default square button with the given text
# Redirects to the event passed in the constructor on click

class Button:
    def __init__(self, x, y, width, height, text, color=(255, 255, 255), text_color=(0, 0, 0), font="None"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.SysFont(font, 32)
        self.text_image = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.rect.center
        
    def draw(self, screen):
        """Draw the button"""
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_image, self.text_rect)
        
    def is_clicked(self, x, y):
        """Return True if the button is clicked"""
        return self.rect.collidepoint(x, y)