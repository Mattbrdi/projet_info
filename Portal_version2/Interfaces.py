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
import sys

info = pygame.display.Info()
largeur = info.current_w
police = pygame.font.Font(None, int(40/1366*largeur))
noir = (0, 0, 0)
white = (255, 255, 255)


# +
# on définit une classe bouton avec plusieurs état d'entrée, un état de sortie, du texte, une zone et un état de sortie secondaire

class bouton:
    def __init__(self, text, rect, etat_sortie, *etats_entree, text_police = police, text_colour = noir, text_center = False, rect_colour = white, contour = False, contour_colour = noir, largeur = 0, etat_sortie_secondaire = False):
        self.etats_entree = etats_entree
        self.etat_sortie = etat_sortie
        self.text = text_police.render(text, True, text_colour)
        self.zone = pygame.Rect(*rect)
        self.rect = rect
        self.zone_colour = rect_colour
        self.contour = contour
        self.largeur = largeur
        self.survol = False
        if text_center:
            self.rect_text = self.text.get_rect(center=text_center)
        else:
            self.rect_text = self.text.get_rect(center=self.zone.center)
        if contour:
            self.rect_contour = pygame.Rect(rect[0] - contour, rect[1] - contour, rect[2] + 2*contour, rect[3] + 2*contour)
            self.contour_colour = contour_colour
        if etat_sortie_secondaire:
            self.etat_sortie_secondaire = etat_sortie_secondaire
        else:
            self.etat_sortie_secondaire = False

# on cherche à savoir si le bouton est survolé par la souris
    
    def est_survole(self, x, y):
        self.survol = self.zone.collidepoint(x, y)


# on affiche le bouton

    def afficher_bouton(self, etat, screen):
        if etat in self.etats_entree:
            if self.survol:
                rectangle = (self.rect[0] - 8, self.rect[1] - 4, self.rect[2] + 16, self.rect[3] + 8)
                contour_rectangle = (self.rect[0] - 9, self.rect[1] - 5, self.rect[2] + 18, self.rect[3] + 10)
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*contour_rectangle))
                pygame.draw.rect(screen, (38, 216, 249), pygame.Rect(*rectangle))
                screen.blit(self.text, self.rect_text)
                return
            if self.contour:
                pygame.draw.rect(screen, self.contour_colour, self.rect_contour)
            pygame.draw.rect(screen, self.zone_colour, self.zone, self.largeur)
            screen.blit(self.text, self.rect_text)

# on définit une classe pour le fond avec un état d'apparition et des paramètres d'affichage
        
class fond:
    def __init__(self, etat, chemin, largeur, hauteur):
        self.etat = etat
        self.image = pygame.transform.scale(pygame.image.load(chemin), (largeur, hauteur))

    def afficher_fond(self, etat1, etat2, screen):
        if self.etat == etat1 or self.etat == etat2:
            screen.blit(self.image, (0, 0))
        
