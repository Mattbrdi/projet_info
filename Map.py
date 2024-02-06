import pygame
import random as rd
 


class Map:
    def __init__(self, filename, carre = 32):
        
        self.map = []
        with open(filename, 'r') as file:
            for line in file:
                self.map.append(list(line)[:-1])
    
        self.PersoAccessibleMatriceCoordinates = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '.':
                    self.PersoAccessibleMatriceCoordinates.append((i, j))
        self.map_decouverte = self.map
        self.carre = carre #un element de la matrice map se dessine en un carré de coté carre


    def draw_map(self, screen):
        for i in range(len(self.map_decouverte)):
            for j in range(len(self.map_decouverte[i])):
                if self.map_decouverte[i][j] == ' ':
                    pygame.draw.rect(screen, (0, 0, 0), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '.':
                    pygame.draw.rect(screen, (255,255,255), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '#':
                    pygame.draw.rect(screen, (100, 100, 100), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '+':
                    pygame.draw.rect(screen, (255,100,100), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '-' or self.map_decouverte[i][j] == '|': 
                    pygame.draw.rect(screen, (0, 0, 255), (j*self.carre, i*self.carre, self.carre, self.carre)) 
    
         
    def get_pos_in_map_matrice(self, position):#retourne l'indice de la case (ligne, colonne)
        return (position[1]//self.carre , position[0]//self.carre)
