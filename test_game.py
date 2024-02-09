import pygame 
import sys
from Perso import personnage
from Map import Map
from test_portail import Portail, portail_select

class Game: 
    def __init__(self):
        pass
         
        
    def run(self, carte_filename):
        """Run the game"""
        carte = Map(carte_filename)
        perso = personnage(carte.spawn) 
        perso.regle_a_la_map(carte) #adapte certaines caracterisique du perso à la map
        
        pygame.init()
        largeur, hauteur = carte.carre*len(carte.map[0]), carte.carre*len(carte.map)
        taille_fenetre = (largeur, hauteur)
        screen = pygame.display.set_mode(taille_fenetre)
        pygame.display.set_caption("screen")
        couleur_fond = (0,0,0)
        blue_portal = Portail(screen, carte_filename, 'blue')
        orange_portal = Portail(screen, carte_filename, 'orange')
        blue_portal.is_selected = True
        running = True
        while running:
            #gerer l'évolution du jeu
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            perso.force_applicated()
            touche = pygame.key.get_pressed()
            portail_select(blue_portal, orange_portal, touche)
            if blue_portal.is_selected:
                perso.handle_key_pressed(touche, blue_portal)
            elif orange_portal.is_selected:
                perso.handle_key_pressed(touche, orange_portal)

            perso.next_position_considering_walls()

            #affichage     
            screen.fill(couleur_fond)
            carte.draw_map(screen)
            perso.draw(screen)
            blue_portal.draw(screen, perso.position, touche)
            orange_portal.draw(screen, perso.position, touche)
            if blue_portal.is_placed:
                blue_portal.keep_drawing(screen)
            if orange_portal.is_placed:
                orange_portal.keep_drawing(screen)
            pygame.event.pump()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
    