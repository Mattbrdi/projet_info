import pygame 
import sys
from Perso import personnage
from Map import Map

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

        running = True
        while running:
            #gerer l'évolution du jeu
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            perso.force_applicated()
            touche = pygame.key.get_pressed()
            perso.handle_key_pressed(touche)
            perso.next_position_considering_walls()
            #affichage     
            screen.fill(couleur_fond)
            carte.draw_map(screen)
            perso.draw(screen)
            pygame.event.pump()

            pygame.display.flip()
            pygame.time.Clock().tick(60)
    