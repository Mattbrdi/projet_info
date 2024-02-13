# +
import pygame

# on récupère les paramètres de l'écran
info = pygame.display.Info()
largeur = info.current_w
hauteur = info.current_h

# on charge l'image dans laquelle on découpe les blocs
image = pygame.transform.scale(pygame.image.load('Photos/Mur_brique.png'), (largeur, hauteur))


# +
# on définit la classe bloc, ce sont des rectangles avec une image à l'intérieur
# on veut les afficher quand le personnage est dans le niveau auquel ils correspondent

class bloc:
    def __init__(self, top_left, width, length, level, remplissage = image):
        self.top_left = top_left
        self.length = length
        self.width = width
        self.zone = pygame.Rect((0, 0, width, length))
        self.image = remplissage.subsurface(self.zone)
        self.level = level

    def afficher_bloc(self, level, screen):
        if self.level == level:
            screen.blit(self.image, self.top_left)

# à partir des blocs du niveau, on construit une matrice indiquant l'état de la surface sur chaque pixel
# l'état vaut 0 si le pixel n'est traversé par aucun côté d'un bloc et un chiffre entre 1 et 4 s'il l'est
# on construit également des listes pour les différentes surfaces sur lequel le joueur peut se cogner 

def surfaces(Blocs, level):
    mat_surface = [[0 for i in range(largeur)] for j in range(hauteur)]
    sols = []
    plafonds = []
    parois_à_gauche = []
    parois_à_droite = []
    Blocs_level = [bloc for bloc in Blocs if bloc.level == level]
    
    for bloc in Blocs_level:
        xg = bloc.top_left[0]
        xd = xg + bloc.width - 1
        yh = bloc.top_left[1]
        yb = yh + bloc.length - 1
        
        sols.append([(xg + i, yh) for i in range(bloc.width)])
        plafonds.append([(xg + i, yb) for i in range(bloc.width)])
        parois_à_gauche.append([(xg, yh + i) for i in range(bloc.length)])
        parois_à_droite.append([(xd, yh + i) for i in range(bloc.length)])
        
        for i in range(bloc.width):
            mat_surface[yh][bloc.top_left[0] + i] = 1
            mat_surface[yb][bloc.top_left[0] + i] = 3
        for i in range(bloc.length):
            mat_surface[yh + i][xg] = 4
            mat_surface[yh + i][xd] = 2
            
    return [mat_surface, sols, parois_à_droite, plafonds, parois_à_gauche]


