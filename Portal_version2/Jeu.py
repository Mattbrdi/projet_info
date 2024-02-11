# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pygame
info = pygame.display.Info()
largeur = info.current_w
hauteur = info.current_h

# on définit pour chaque niveau un spawn 

levels = {'Level_1': (3*int(30/1366*largeur), 3*int(hauteur/8) - int(30/1366*largeur)),
         'Level_2': (3*int(30/1366*largeur), 3*int(hauteur/8) - int(30/1366*largeur)),
         'Level_3': (3*int(30/1366*largeur), 3*int(hauteur/8) - int(30/1366*largeur))}

# on choisit les couleurs des portails

couleurs = ((78, 158, 221), (255, 179, 71))

coeff1 = largeur/1366
coeff2 = hauteur/768

# on définit des grandeurs pour la dynamique
# le personnage recule quand il se contraint par une paroi

g = -0.1*coeff2
v_saut = 2*coeff2
x_contraint = 1*coeff1
y_contraint = 1*coeff2
v_deplacement = 2*coeff1
v_max = 12*coeff2


# +
# on définit la classe personnage avec une position, une vitesse, un rayon et deux états de contrainte

class perso:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.v_x = 0
        self.v_y = 0
        self.y_state = 'touche_le_sol'
        self.x_state = 'libre'
        self.rayon = int(20/1366*largeur)

# on charge la position de spawn au début du niveau

    def debut_level(self, level):
        self.x = levels[level][0]
        self.y = levels[level][1]

# on définit une fonction pour savoir si le personnage se cogne à une paroi
    
    def collision(self, surface):
        for x, y in surface:
            if (self.x - x)**2 + (self.y - y)**2 <= self.rayon**2:
                return True
        return False

# cette fonction permet de déterminer les états de contrainte du personnage
    
    def etat_perso(self, sols, parois_à_droite, plafonds, parois_à_gauche):
        self.y_state = "en_l'air"
        if sum(self.collision(sol) for sol in sols):
            self.y_state = 'touche_le_sol'
        if sum(self.collision(plafond) for plafond in plafonds):
            self.y_state = 'touche_le_plafond'
            
        if sum(self.collision(paroi) for paroi in parois_à_droite):
            self.x_state = 'contraint_à_gauche'
        elif sum(self.collision(paroi) for paroi in parois_à_gauche):
            self.x_state =  'contraint_à_droite'
        else:
            self.x_state = 'libre'

# ces étas de contrainte et les touches du clavier permmettent de déterminer la déplacement du personnage
# les boutons permettant de se déplacer latéralement ne sont effectifs qu'aux petites vitesses
# cela permet une meilleure intéraction entre le joueur et les portails
# Notamment, le joueur conserve sa vitesse si elle est grande en empruntant un portail et peut donc accélérer en tombant sans fin
# Il est néanmoins limité par une vitesse maximale qu'il ne peut dépasser


    def deplacement(self, touches_pressees):
        if self.y_state == 'touche_le_plafond':
            self.v_y = 0
            self.y += y_contraint
        self.v_y += g
        
        if self.y_state == 'touche_le_sol':
            self.v_y = 0
            self.v_x = 0
            if touches_pressees[pygame.K_UP]:
                self.v_y = v_saut

        if touches_pressees[pygame.K_RIGHT] and abs(self.v_x) <= v_deplacement and self.v_x < v_deplacement:
            self.v_x += v_deplacement
        if touches_pressees[pygame.K_LEFT] and abs(self.v_x) <= v_deplacement and self.v_x > -v_deplacement: 
            self.v_x -= v_deplacement 

        if self.x < self.rayon:
            self.v_x = 0
            self.x += x_contraint
        if self.x_state == 'contraint_à_droite':
            self.v_x = min(0, self.v_x)
            self.x -= x_contraint
            
        if self.x_state == 'contraint_à_gauche':
            self.v_x = max(0, self.v_x)
            self.x += x_contraint

        if self.v_y >= 0:
            self.v_y = min(self.v_y, v_max)
        else:
            self.v_y = max(self.v_y, -v_max)
        if self.v_x >= 0:
            self.v_x = min(self.v_x, v_max)
        else:
            self.v_x = max(self.v_x, -v_max)
        
        self.x += self.v_x
        self.y -= self.v_y

    def afficher_perso(self, screen):
        pygame.draw.circle(screen, (78, 158, 221), (self.x, self.y), self.rayon)
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.rayon, 2)

# la traversée des portails par le personnage dépend de l'état de surface du portail de sorie
# En effet, le personnage va être téléporté et sa vitesse va être redéfinie en fonction de cet état de surface
# Si elle est grande, le personnage conserve sa vitesse, 
# Sinon, on lui en attribue une nouvelle qui l'empêche de rentrer et sortir indéfiniment des portails

    def traverser_portail(self, portails):
        portail0, portail1 = portails
        if portail0.etat_du_portail and portail1.etat_du_portail:
            if (portail0.x - self.x)**2 + (portail0.y - self.y)**2 <= (self.rayon*7/6)**2:
                if portail1.etat_surface % 2 == 1:
                    self.x = portail1.x
                    self.y = portail1.y + (portail1.etat_surface - 2)*(self.rayon*4/3)
                    self.v_y = -(portail1.etat_surface - 2)*max((self.v_y**2 + self.v_x**2)**(1/2), 2*v_saut)
                    self.v_x = 0
                if portail1.etat_surface %2 == 0:
                    self.x = portail1.x - (portail1.etat_surface - 3)*(self.rayon*4/3)
                    self.y = portail1.y - 5
                    self.v_x = -(portail1.etat_surface - 3)*max((self.v_y**2 + self.v_x**2)**(1/2), 3/2*v_deplacement)
                    self.v_y = 0
                    
            if (portail1.x - self.x)**2 + (portail1.y - self.y)**2 <= (self.rayon*7/6)**2:
                if portail0.etat_surface % 2 == 1:
                    self.x = portail0.x
                    self.y = portail0.y + (portail0.etat_surface - 2)*(self.rayon*4/3)
                    self.v_y = -(portail0.etat_surface - 2)*max((self.v_y**2 + self.v_x**2)**(1/2), 2*v_saut)
                    self.v_x = 0
                if portail0.etat_surface %2 == 0:
                    self.x = portail0.x - (portail0.etat_surface - 3)*(self.rayon*4/3)
                    self.y = portail0.y - 5 
                    self.v_x = -(portail0.etat_surface - 3)*max((self.v_y**2 + self.v_x**2)**(1/2), 3/2*v_deplacement)
                    self.v_y = 0

# Si le personnage arrive à la fin de la carte, il gagne et sa vitesse est réinitialisée
                    
    def victoire(self, screen_state):
        if self.x > largeur - self.rayon:
            screen_state.current_state = 'victoire'
            self.v_x = 0
            self.v_y = 0
            
# on définit une ultime fonciton qui regroupe les fonctions ci-dessus

    def gestion_perso(self, sols, parois_à_droite, plafonds, parois_à_gauche, touches_pressees, screen, portails, screen_state):
        self.etat_perso(sols, parois_à_droite, plafonds, parois_à_gauche)
        self.deplacement(touches_pressees)
        self.traverser_portail(portails)
        self.victoire(screen_state)
        self.afficher_perso(screen)

# on définit une classe pour les portails, on retient s'il est posé, sur quelle surface et le prochain portail à envoyer

class portail:
    def __init__(self, couleur):
        self.x = 0
        self.y = 0
        self.etat_surface = 0
        self.etat_des_portails = 0
        self.etat_du_portail = False
        self.couleur = couleur
        self.rect_ovale = 0

# on définit une fonction qui actualise les paramètres du portail quand il est lancé
        
    def lancer_portail(self, arrivee, etat_surface):
        self.etat_du_portail = True
        self.etat_surface = etat_surface
        if etat_surface % 2 == 1:
            self.rect_ovale = pygame.Rect(arrivee[0] - int(45/1366*largeur), arrivee[1] - int(10/1366*largeur), int(90/1366*largeur), int(20/1366*largeur))
        else:
            self.rect_ovale = pygame.Rect(arrivee[0] - int(10/1366*largeur), arrivee[1] - int(45/1366*largeur), int(20/1366*largeur), int(90/1366*largeur))
        self.x, self.y = arrivee

# on affiche les portails lancés

    def afficher_portail(self, screen):
        if self.etat_du_portail:
            pygame.draw.ellipse(screen, (0, 0, 0), self.rect_ovale)
            pygame.draw.ellipse(screen, self.couleur, self.rect_ovale, width = int(5/1366*largeur))

            
# on définit cette fonction pour plus de style

def ligne_pointillée(screen, couleur, depart, arrivee, longueur = int(8/1366*largeur), espace = int(8/1366*largeur)):
    x1, y1 = depart
    x2, y2 = arrivee
    dx = x2 - x1
    dy = y2 - y1
    distance = max(abs(dx), abs(dy))
    if distance == 0:
        return 
    dx = dx / distance
    dy = dy / distance
    x = x1
    y = y1
    for _ in range(int(distance / (longueur + longueur))):
        pygame.draw.line(screen, couleur, (int(x), int(y)), (int(x + dx * longueur), int(y + dy * longueur)))
        x += dx * (longueur + longueur)
        y += dy * (longueur + longueur)

# pour lancer les portails le joueur a le droit à un viseur
# il apparaît quand certaines touches sont pressées et sa couleur dépend de la couleur du prochain portail à lancer
# il commence au centre du personnage et s'arrête au premier obstacle
# s'il n'y a pas d'obstacle, il s'arrête à la fin de la carte

class viseur:
    def __init__(self, couleur = (38, 216, 249)):
        self.direction = [0, 0]
        self.depart = (0, 0)
        self.arrivee = (0, 0)
        self.couleur = couleur
        self.state = False
        self.etat_des_portails = 0

    def def_direction(self, touches_pressees):
        self.direction = [0, 0]
        if touches_pressees[pygame.K_d]:
            self.direction[0] += 1
        if touches_pressees[pygame.K_s]:
            self.direction[1] += 1
        if touches_pressees[pygame.K_q]:
            self.direction[0] -= 1
        if touches_pressees[pygame.K_z]:
            self.direction[1] -= 1
        self.state = bool(self.direction[0] or self.direction[1])

    def def_depart(self, x, y):
        self.depart = (x, y)

    def arrivee_et_affichage(self, mat_surfaces, screen):
        xd, yd = self.depart
        if self.state:
            while 0 < xd < largeur - 1 and 0 < yd < hauteur - 1 and not mat_surfaces[int(yd)][int(xd)]:
                xd += self.direction[0]
                yd += self.direction[1]
            self.arrivee = (xd, yd)
            ligne_pointillée(screen, self.couleur, self.depart, self.arrivee)

# on regroupe toutes les fonctions ci_dessus dans celle-ci
    
    def gestion_viseur(self, touches_pressees, x, y, mat_surfaces, screen, events, portails):
        self.def_direction(touches_pressees)
        self.def_depart(x, y)
        self.arrivee_et_affichage(mat_surfaces, screen)
        etat_surface = mat_surfaces[int(self.arrivee[1])][int(self.arrivee[0])]
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.state and etat_surface:
                    portails[self.etat_des_portails].lancer_portail(self.arrivee, etat_surface)
                    self.etat_des_portails = 1 - self.etat_des_portails
                    self.couleur = couleurs[self.etat_des_portails]
                    
                    
            
        
