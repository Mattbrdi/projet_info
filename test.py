import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
window_width = 400
window_height = 300

# Créer une surface avec une couleur de fond blanche
my_surface = pygame.Surface((100, 50))
my_surface.fill((0, 255, 255))  # Remplir la surface avec du blanc

# Dessiner une ellipse rouge sur la surface
pygame.draw.ellipse(my_surface, (255, 0, 0), my_surface.get_rect(), 2)

# Créer un objet Rect pour définir la position de la surface à l'écran
my_rect = my_surface.get_rect()
my_rect.topleft = (0, 0)  # Définir la position en haut à gauche de la surface

# Initialiser la fenêtre
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Exemple Pygame")

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    window.fill((255, 255, 255))

    # Afficher la surface à la position spécifiée par le Rect
    window.blit(my_surface, my_rect.topleft)

    # Mettre à jour l'affichage
    pygame.display.flip()
