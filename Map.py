import pygame
import random as rd
 


class Map:
    def __init__(self, filename, carre = 32):
        
        self.map = []
        with open(filename, 'r') as file:
            for line in file:
                self.map.append(list(line)[:-1])
                
        self.carre = carre #un element de la matrice map se dessine en un carré de coté carre
        
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '@':
                    self.spawn = (j*self.carre +(self.carre //2 ) , (i+1)*self.carre-1)
        self.map_decouverte = self.map #sert si jamais on fait une map evolutive
        

    def draw_map(self, screen):
        for i in range(len(self.map_decouverte)):
            for j in range(len(self.map_decouverte[i])):
                if self.map_decouverte[i][j] == ' ':
                    pygame.draw.rect(screen, (0, 0, 0), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '.': #zone accessible
                    pygame.draw.rect(screen, (255,255,255), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '@': #spawn
                    pygame.draw.rect(screen, (100, 100, 100), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '+': #premier mur (differend des autres murs car pas colorié)
                    pygame.draw.rect(screen, (255,255,255), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '-' or self.map_decouverte[i][j] == '|': #mur
                    pygame.draw.rect(screen, (0, 0, 255), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == 'P': #Fin du niveau
                    pygame.draw.rect(screen, (0, 255, 0), (j*self.carre, i*self.carre, self.carre, self.carre))
