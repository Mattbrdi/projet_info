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
pygame.init()
import Statemachine
import Interfaces
import Carte
import Jeu

# on initialise des paramètres d'affichage des boutons, des fonds, des blocs

pygame.display.set_caption("Portal")
info = pygame.display.Info()
largeur = info.current_w
hauteur = info.current_h
largeur_bouton = int(largeur*200/1366)
hauteur_bouton = int(hauteur*50/768)
x_milieu = int((largeur-largeur_bouton)/2)
y_milieu = int((hauteur-hauteur_bouton)/2)
screen = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()
temps_debut = [0]
en_cours = True
police = pygame.font.Font(None, int(40/1366*largeur))
noir = (0, 0, 0)
white = (255, 255, 255)
perso = Jeu.perso()
surfaces = [[]]
viseur = Jeu.viseur()
portail0 = Jeu.portail((78, 158, 221))
portail1 = Jeu.portail((255, 179, 71))
pygame.mixer.music.load("Musiques/Portal_menu.mp3")
pygame.mixer.music.play(-1)       


Play = Interfaces.bouton('Jouer', (x_milieu, y_milieu, largeur_bouton, hauteur_bouton), 'levels', 'menu', largeur = 1, text_colour = white)
Touches = Interfaces.bouton('Touches', (x_milieu, y_milieu + int(3/2*hauteur_bouton), largeur_bouton, hauteur_bouton), 'touches', 'menu', largeur = 1, text_colour = white)
Musique = Interfaces.bouton('Musique', (x_milieu, y_milieu + 3*hauteur_bouton, largeur_bouton, hauteur_bouton), 'musique', 'menu', largeur = 1, text_colour = white)
Level1 = Interfaces.bouton('Niveau 1', (x_milieu, y_milieu + int(3/2*hauteur_bouton), largeur_bouton, hauteur_bouton), 'jeu', 'levels', etat_sortie_secondaire = 'Level_1', largeur = 1, text_colour = white)
Level2 = Interfaces.bouton('Niveau 2', (x_milieu, y_milieu + 3*hauteur_bouton, largeur_bouton, hauteur_bouton), 'jeu', 'levels', etat_sortie_secondaire = 'Level_2', largeur = 1, text_colour = white)
Level3 = Interfaces.bouton('Niveau 3', (x_milieu, y_milieu + int(9/2*hauteur_bouton), largeur_bouton, hauteur_bouton), 'jeu', 'levels', etat_sortie_secondaire = 'Level_3', largeur = 1, text_colour = white)
Menu = Interfaces.bouton('Menu', (x_milieu, y_milieu - hauteur_bouton, largeur_bouton, hauteur_bouton), 'menu', 'victoire', 'levels', 'touches', largeur = 1, text_colour = white)
Quit = Interfaces.bouton('Quitter', (x_milieu, y_milieu + int(9/2*hauteur_bouton), largeur_bouton, hauteur_bouton), 'quit', 'menu', largeur = 1, text_colour = white)


fond1 = Interfaces.fond('menu', 'Photos/accueil.jpg', largeur, hauteur)
fond2 = Interfaces.fond('levels', 'Photos/accueil.jpg', largeur, hauteur)
fond3 = Interfaces.fond('touches', 'Photos/accueil.jpg', largeur, hauteur)
fond4 = Interfaces.fond('settings', 'Photos/accueil.jpg', largeur, hauteur)
fond5 = Interfaces.fond('victoire', 'Photos/accueil.jpg', largeur, hauteur)

Bloc1 = Carte.bloc((0, hauteur - int(hauteur/16)), largeur, int(hauteur/16), 'Level_1')
Bloc2 = Carte.bloc((2*int(largeur/16), 4*int(hauteur/16)), 2*int(largeur/16), 11*int(hauteur/16), 'Level_1')
Bloc3 = Carte.bloc((0, 0), largeur, int(hauteur/16), 'Level_1')
Bloc4 = Carte.bloc((6*int(largeur/16), 1*int(hauteur/16)), 2*int(largeur/16), 12*int(hauteur/16), 'Level_1')
Bloc5 = Carte.bloc((10*int(largeur/16), 3*int(hauteur/16)), 2*int(largeur/16), 12*int(hauteur/16), 'Level_1')
Bloc6 = Carte.bloc((largeur-2*int(largeur/16), int(hauteur/16)), 2*int(largeur/16), 12*int(hauteur/16), 'Level_1')
Bloc7 = Carte.bloc((12*int(largeur/16), 8*int(hauteur/16)), int(largeur/16) - int(10/1366*largeur), int(hauteur/16), 'Level_1')
Bloc8 = Carte.bloc((13*int(largeur/16) + int(20/1366*largeur), 8*int(hauteur/16)), int(largeur/16) - int(10/1366*largeur), int(hauteur/16), 'Level_1')

Bloc10 = Carte.bloc((0, hauteur - int(hauteur/16)), largeur, int(hauteur/16), 'Level_2')
Bloc11 = Carte.bloc((2*int(largeur/16), 5*int(hauteur/16)), int(largeur/32), 10*int(hauteur/16), 'Level_2')
Bloc12 = Carte.bloc((2*int(largeur/16), 4*int(hauteur/16)), 2*int(largeur/16), int(hauteur/16), 'Level_2')
Bloc13 = Carte.bloc((4*int(largeur/16) + int(20/1366*largeur), 4*int(hauteur/16)), 2*int(largeur/16), int(hauteur/16), 'Level_2')
Bloc14 = Carte.bloc((0, 0), int(largeur/2), int(hauteur/16), 'Level_2')
Bloc15 = Carte.bloc((6*int(largeur/16), 1*int(hauteur/16)), int(largeur/32), 13*int(hauteur/16), 'Level_2')
Bloc16 = Carte.bloc((9*int(largeur/16), 5*int(hauteur/16)), int(largeur/32), 10*int(hauteur/16), 'Level_2')
Bloc17 = Carte.bloc((9*int(largeur/16), 4*int(hauteur/16)), 6*int(largeur/16), int(hauteur/16), 'Level_2')
Bloc18 = Carte.bloc((largeur - int(largeur/32), 0), int(largeur/32), 14*int(hauteur/16), 'Level_2')
Bloc19 = Carte.bloc((largeur - 4*int(largeur/16), 8*int(hauteur/16)), 4*int(largeur/16), int(hauteur/16), 'Level_2')
Bloc20 = Carte.bloc((9*int(largeur/16), 8*int(hauteur/16)), 3*int(largeur/16) - int(20/1366*largeur), int(hauteur/16), 'Level_2')
Bloc21 = Carte.bloc((29*int(largeur/32), 11*int(hauteur/16)), int(largeur/32), 4*int(hauteur/16), 'Level_2')

Bloc25 = Carte.bloc((0, hauteur - int(hauteur/16)), largeur, int(hauteur/16), 'Level_3')
Bloc26 = Carte.bloc((2*int(largeur/16), 5*int(hauteur/16)), int(largeur/32), 10*int(hauteur/16), 'Level_3')
Bloc27 = Carte.bloc((2*int(largeur/16), 4*int(hauteur/16)), 2*int(largeur/16), int(hauteur/16), 'Level_3')
Bloc28 = Carte.bloc((4*int(largeur/16) + int(20/1366*largeur), 4*int(hauteur/16)), 2*int(largeur/16) - int(20/1366*largeur), int(hauteur/16), 'Level_3')
Bloc29 = Carte.bloc((0, 0), int(largeur/32), hauteur, 'Level_3')
Bloc30 = Carte.bloc((6*int(largeur/16), 0), int(largeur/32), 14*int(hauteur/16), 'Level_3')
Bloc31 = Carte.bloc((8*int(largeur/16), 11*int(hauteur/32)), int(largeur/32), 19*int(hauteur/32), 'Level_3')
Bloc32 = Carte.bloc((6*int(largeur/16), 4*int(hauteur/16)), 10*int(largeur/16), 1*int(hauteur/16), 'Level_3')
Bloc33 = Carte.bloc((10*int(largeur/16), 5*int(hauteur/16)), int(largeur/32), 8*int(hauteur/16), 'Level_3')
Bloc34 = Carte.bloc((10*int(largeur/16), 14*int(hauteur/16) - int(20/1366*largeur)), int(largeur/32), int(hauteur/16) + int(20/1366*largeur), 'Level_3')
Bloc35 = Carte.bloc((12*int(largeur/16), 6*int(hauteur/16)), int(largeur/16), 9*int(hauteur/16), 'Level_3')


Blocs = [Bloc1, Bloc2, Bloc3, Bloc4, Bloc5, Bloc6, Bloc7, Bloc8,
        Bloc10, Bloc11, Bloc12, Bloc13, Bloc14, Bloc15, Bloc16, Bloc17, Bloc18, Bloc19, Bloc20, Bloc21,
        Bloc25, Bloc26, Bloc27, Bloc28, Bloc29, Bloc30, Bloc31, Bloc32, Bloc33, Bloc34, Bloc35]

boutons = [Play, Touches, Level1, Level2, Level3, Menu, Musique, Quit]
fonds = [fond1, fond2, fond3, fond4, fond5]
screen_state = Statemachine.machine('menu')

# on définit une fonction supplémentaire pour gérer certaines transitions 

def transiter(screen_state):
    if screen_state.transition == ('levels', 'jeu'):
        surfaces[0] = Carte.surfaces(Blocs, screen_state.secondary_state)
        temps_debut[0] = temps_actuel
        perso.debut_level(screen_state.secondary_state)
    if screen_state.secondary_state == 'Level_1' and screen_state.musique:
        pygame.mixer.music.load("Musiques/Portal_level1.mp3")
        pygame.mixer.music.play(-1)
    if screen_state.secondary_state == 'Level_2' and screen_state.musique:
        pygame.mixer.music.load("Musiques/Portal_level2.mp3")
        pygame.mixer.music.play(-1)
    if screen_state.secondary_state == 'Level_3' and screen_state.musique:
        pygame.mixer.music.load("Musiques/Portal_level3.mp3")
        pygame.mixer.music.play(-1)
    if screen_state.current_state == 'menu' and screen_state.musique and screen_state.transition != ('touches', 'menu'):
        pygame.mixer.music.load("Musiques/Portal_menu.mp3")
        pygame.mixer.music.play(-1)


while en_cours:
    clock.tick(200)
    temps_actuel = pygame.time.get_ticks()
    souris_x, souris_y = pygame.mouse.get_pos()
    screen.fill(noir)
    
    # on regarde si le joueur clique sur un bouton et quelle transition cela entraîne
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen_state.reset_compteur()
            for bouton in boutons:
                screen_state.click(event, bouton)
            if screen_state.cpt_transition:
                transiter(screen_state)

    # on affiche les fonds, les blocs et les boutons
                
    for fond in fonds:
        fond.afficher_fond(screen_state.current_state, screen_state.secondary_state, screen)
    
    for bloc in Blocs:
        bloc.afficher_bloc(screen_state.secondary_state, screen)
        
    for bouton in boutons:
        bouton.afficher_bouton(screen_state.current_state, screen)
        bouton.est_survole(souris_x, souris_y)

        
    if screen_state.current_state == 'quit':
        en_cours = False

    # on gère le compteur de temps ici et on appelle les fonctions nécessaires au déroulement du jeu

    if screen_state.current_state == 'jeu':
        perso.gestion_perso(surfaces[0][1], surfaces[0][2], surfaces[0][3], surfaces[0][4], pygame.key.get_pressed(), screen, (portail0, portail1), screen_state)
        viseur.gestion_viseur(pygame.key.get_pressed(), perso.x, perso.y, surfaces[0][0], screen, pygame.event.get(), (portail0, portail1))
        portail0.afficher_portail(screen)
        portail1.afficher_portail(screen)
        temps_ecoule = temps_actuel - temps_debut[0]
        temps_ecoule_secondes = temps_ecoule // 1000
        texte_temps = police.render(f"Temps écoulé : {temps_ecoule_secondes} s", True, (255, 255, 255))
        rect_temps = pygame.Rect((int(largeur/16), int(hauteur/64), largeur_bouton, hauteur_bouton))
        rect_temps_texte = texte_temps.get_rect(center= rect_temps.center)
        screen.blit(texte_temps, rect_temps_texte)

    if screen_state.current_state == 'victoire':
        screen.blit(texte_temps, rect_temps_texte)

    # on applique les propriétés propres au reste des états

    screen_state.appliquer_etat(screen, largeur, hauteur, portail0, portail1)
        
    pygame.display.update()

pygame.quit()


