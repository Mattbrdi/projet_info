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


noir = (0, 0, 0)
white = (255, 255, 255)


# +
# on définit une classe machine car on a besoin d'une machine à états pour gérer l'affichage
# on retient l'état du jeu, le sous-état du jeu (pour connaître le niveau) et si la musique est activée, 
# on retient la dernière transition d'états et un booléen pour savoir si la transition si récente

class machine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.musique = True
        self.secondary_state = 'None'
        self.transition = (initial_state, initial_state)
        self.cpt_transition = False

# on effectue des transitions en fonction des boutons sur lesquels le joueur a cliqué
# le bouton musique est géré un peu différement
    
    def click(self, event, bouton):
        if (not self.cpt_transition) and self.current_state in bouton.etats_entree and bouton.zone.collidepoint(event.pos):
            self.transition = (self.current_state, bouton.etat_sortie)
            self.current_state = bouton.etat_sortie
            self.cpt_transition = True
            if bouton.etat_sortie_secondaire:
                self.secondary_state= bouton.etat_sortie_secondaire
                
        if self.current_state == 'musique':
            self.current_state = 'menu'
            self.musique = not self.musique
            if self.musique:
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.stop()

    def reset_compteur(self):
        self.cpt_transition = False    

# on réalise certaines actions en fonction de l'état du jeu
    
    def appliquer_etat(self, screen, largeur, hauteur, portail0, portail1):
            
        if self.current_state == 'menu':
            texte_titre = pygame.font.Font(None, int(300/1366*largeur)).render('Portal', True, (38, 216, 249))
            rect_titre = texte_titre.get_rect(center=(int(largeur/2), int(hauteur/4)))
            screen.blit(texte_titre, rect_titre)
            
        if not self.current_state == 'jeu':
            self.secondary_state = 'None'

        if self.current_state == 'victoire':
            portail0.etat_du_portail = False
            portail1.etat_du_portail = False
            texte_titre = pygame.font.Font(None, int(300/1366*largeur)).render('Victoire !', True, (38, 216, 249))
            rect_titre = texte_titre.get_rect(center=(int(largeur/2), int(hauteur/4)))
            screen.blit(texte_titre, rect_titre)
            
        if self.current_state == 'touches':
            
            ligne1 = "Sauter : Flèche du haut"
            ligne2 = "Avancer à droite : Flèche de droite"
            ligne3 = "Avancer à gauche : Flèche de gauche"
            ligne4 = "Orienter le viseur : Z, Q, S, D"
            ligne5 = "Lancer un portial : Espace"
            ligne1_surface = pygame.font.Font(None, int(50/1366*largeur)).render(ligne1, True, white)
            ligne1_rect = ligne1_surface.get_rect(center=(int(largeur/2), 6*int(hauteur/12)))
            ligne2_surface = pygame.font.Font(None, int(50/1366*largeur)).render(ligne2, True, white)
            ligne2_rect = ligne1_surface.get_rect(center=(int(largeur/2), 7*int(hauteur/12)))
            ligne3_surface = pygame.font.Font(None, int(50/1366*largeur)).render(ligne3, True, white)
            ligne3_rect = ligne1_surface.get_rect(center=(int(largeur/2), 8*int(hauteur/12)))
            ligne4_surface = pygame.font.Font(None, int(50/1366*largeur)).render(ligne4, True, white)
            ligne4_rect = ligne1_surface.get_rect(center=(int(largeur/2), 9*int(hauteur/12)))
            ligne5_surface = pygame.font.Font(None, int(50/1366*largeur)).render(ligne5, True, white)
            ligne5_rect = ligne1_surface.get_rect(center=(int(largeur/2), 10*int(hauteur/12)))
            screen.blit(ligne1_surface, ligne1_rect)
            screen.blit(ligne2_surface, ligne2_rect)
            screen.blit(ligne3_surface, ligne3_rect)
            screen.blit(ligne4_surface, ligne4_rect)
            screen.blit(ligne5_surface, ligne5_rect)
