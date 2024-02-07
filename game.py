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
        print("---------------------",carte.spawn)
        perso = personnage(carte.spawn) 
        perso.def_accessible_coordinates(carte)
        
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
                perso.handle_event(event)
                
                
            #perso.next_position_considering_walls()
            
            #affichage     
            screen.fill(couleur_fond)
            carte.draw_map(screen)
            perso.draw(screen)
            for pixel in perso.AccessibleCoordinates:
                screen.set_at(pixel, (0,255,0))
            print(perso.position in perso.AccessibleCoordinates)
            pygame.display.flip()
            pygame.time.Clock().tick(20)
    