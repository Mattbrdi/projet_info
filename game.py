import pygame 
import sys
import Perso 
class Game: 
    def __init__(self):
        pass
    
    def handle_events(self, event):
        direction = None
        Space = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"
            elif event.key == pygame.K_SPACE:
                Space = True 
    
    def run(self):
        """Run the game"""
        pygame.init()
        largeur, hauteur = carre*len(carte.map[0]), carre*len(carte.map)
        taille_fenetre = (largeur, hauteur)
        screen = pygame.display.set_mode(taille_fenetre)
        pygame.display.set_caption("screen")
        couleur_fond = (0,0,0)


        running = True
        while running:
            direction = None
            Space = False
            for event in pygame.event.get():
                self.handle_events(event)
                  
            screen.fill(couleur_fond)
            pygame.update_display(screen, 32, (255, 0, 0), perso)
           

            pygame.display.flip()
            pygame.time.Clock().tick(20)
    