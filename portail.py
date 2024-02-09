import pygame


def select_portal(portal_1, portal_2, keys):
    """
    Permet de sélectionner un portail à la fois
    """
    assert portal_1.is_selected != portal_2.is_selected
    if keys[pygame.K_TAB]:
        if portal_1.is_selected:
            portal_1.is_selected = False
            portal_2.is_selected = True
        else:
            portal_1.is_selected = True
            portal_2.is_selected = False


def choose_color(color):
    """
    Choix de la couleur du portail
    """
    if color == 'blue':
        return (0, 255, 255)
    if color == 'orange':
        return (255, 100, 0)


def get_tile_normal(grid, x, y):
    """
    Renvoie la direction de la surface du portail qui est la normale à la surface
    sur laquelle le portail est placé
    """
    if x > 0 and grid[y][x - 1] == '.':  # Il y a une case vide à gauche
        return (-1, 0)
    elif x < len(grid[0]) - 1 and grid[y][x + 1] == '.':  # Il y a une case vide à droite
        return (1, 0)
    elif y > 0 and grid[y - 1][x] == '.':  # Il y a une case vide au dessus
        return (0, -1)
    elif y < len(grid) - 1 and grid[y + 1][x] == '.':  # Il y a une case vide en dessous
        return (0, 1)
    else:
        return (-1, 0)  # Si aucune case vide n'est trouvée, on retourne la normale par défaut
    

def dilatation(text_file, factor):
    """
    Cette fonction prend un fichier texte qui représente la map et le dilate par 
    un facteur donné. Nous en aurons besoin pour pouvoir placer les portails sur la carte
    
    Parameters : 
    text_file (.txt) : le fichier texte qui représente la map
    factor (int) : le facteur de dilatation

    Returns : 
    array (list) : la map dilatée
    """
    with open(text_file, 'r') as file:
        array = [list(line.strip().replace('@', '.')) for line in file] 
    return [[char for char in row for _ in range(factor)] for row in array for _ in range(factor)]

"""
Ce dictionnaire permet de corriger le placement des portails sur la carte en fonciton 
de l'orientation de ces derniers
"""
pos = {'up':     [-29, 25 , 60, 14], 
       'down':   [-29, -38, 60, 14], 
       'left':   [25, -28, 14, 60], 
        'right': [-38, -28, 14, 60],
      }
 
class Portail:
    """
    La classe portail permet de créer un portail, de la placer sur la carte 
    et de le déplacer

    Parameters : 

    screen (pygame.Surface) : la fenêtre de jeu
    carte (str) : le fichier texte qui représente la map
    color (str) : la couleur du portail
    """
    def __init__(self, screen, carte, color):
        self.x = 0 
        self.y = 0 
        self.screen = screen 
        self.map = dilatation(carte, 32)
        self.color = color 
        self.drawing_color = choose_color(self.color)
        self.facing = 'none'
        self.is_selected = False 
        self.is_placed = False
    
    #TODO : the int position may not be the position of the character
    def get_draw_position(self, touches, position):
        """
        Cette fonction permet de placer le portail sur la carte en fonction de la
        direction dans laquelle le joueur veut le placer.

        Parameters :
        touches (dict) : les touches du clavier appuyées
        position (list) : la position du personnage

        Returns :
        int_position (list) : la position du portail sur la carte
        """
        int_position = [int(position[0]), int(position[1])]
        i = int_position[1]
        j = int_position[0]
        max_i = len(self.map) - 1
        max_j = len(self.map[0]) - 1
        if touches[pygame.K_z] and not touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_s]:
            while self.map[i][j] == '.' and i >= 0:
                i -= 1
        elif touches[pygame.K_s] and not touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_z]:
            while self.map[i][j] == '.' and i <= max_i:
                i += 1
        elif touches[pygame.K_q] and not touches[pygame.K_z] and not touches[pygame.K_s] and not touches[pygame.K_d]:
            while self.map[i][j] == '.' and j >= 0:
                j -= 1
        elif touches[pygame.K_d] and not touches[pygame.K_z] and not touches[pygame.K_s] and not touches[pygame.K_q]:
            while self.map[i][j] == '.' and j <= max_j:
                j += 1
        elif touches[pygame.K_z] and touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_s]:
            while self.map[i][j] == '.' and i >= 0 and j >= 0:
                i -= 1
                j -= 1
        elif touches[pygame.K_z] and touches[pygame.K_d] and not touches[pygame.K_q] and not touches[pygame.K_s]:
            while self.map[i][j] == '.' and i >= 0 and j <= max_j:
                i -= 1
                j += 1
        elif touches[pygame.K_s] and touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_z]:
            while self.map[i][j] == '.' and i <= max_i and j >= 0:
                i += 1
                j -= 1
        elif touches[pygame.K_s] and touches[pygame.K_d] and not touches[pygame.K_q] and not touches[pygame.K_z]:
            while self.map[i][j] == '.' and i <= max_i and j <= max_j:
                i += 1
                j += 1
        return j, i

    def get_portal_facing(self, surface_normal):
        """
        Cette fonction permet de déterminer l'orientation du portail en fonction de la
        normale de la surface sur laquelle il est placé.

        Parameters :
        surface_normal (tuple) : la normale de la surface sur laquelle le portail est placé

        Returns :
        str : l'orientation du portail
        """
        if surface_normal == (0, -1):
            return 'up'
        elif surface_normal == (0, 1):
            return 'down'
        elif surface_normal == (-1, 0):
            return 'left'
        elif surface_normal == (1, 0):
            return 'right'
        else:
            return 'left'  # Si aucune case vide n'est trouvée, on retourne la normale par défaut

    def draw(self, screen, position, touches):
        """
        Cette fonction permet de dessiner le portail sur la carte en fonction de la
        direction dans laquelle le joueur veut le placer.
        
        Parameters :
        screen (pygame.Surface) : la fenêtre de jeu
        position (list) : la position du personnage
        touches (dict) : les touches du clavier appuyées
        """
        if self.is_selected:
            if touches[pygame.K_SPACE]:
                self.x, self.y = self.get_draw_position(touches, position)
                self.facing = self.get_portal_facing(get_tile_normal(self.map, self.x, self.y))
                if touches[pygame.K_z] or touches[pygame.K_s] or touches[pygame.K_q] or touches[pygame.K_d]:
                    self.is_placed = True
                    self.keep_drawing(screen)
                    
    def keep_drawing(self, screen):
        """
        Cette fonction permet de garder le portail dessiné sur la carte
        Parameters:
        screen (pygame.Surface) : la fenêtre de jeu

        Note:
        Cette fonciton utilise le dictionnaire 'pos' pour corriger le placement du portail 
        en fonction de l'orientation de ce dernier
        """
        rect_ovale = pygame.Rect(self.x + pos[self.facing][0], self.y + pos[self.facing][1], pos[self.facing][2], pos[self.facing][3])
        pygame.draw.ellipse(screen, self.drawing_color, rect_ovale)

    
        
