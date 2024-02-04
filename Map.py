import pygame
import random as rd
 


class Map:
    def __init__(self, filename, carre = 32):
        
        self.map = []
        with open(filename, 'r') as file:
            for line in file:
                self.map.append(list(line)[:-1])
    
        accessibleCoordinates = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '.':
                    accessibleCoordinates.append((i, j))

        self.map_decouverte = self.map
        self.carre = carre


    def draw_map(self, screen):
        for i in range(len(self.map_decouverte)):
            for j in range(len(self.map_decouverte[i])):
                if self.map_decouverte[i][j] == ' ':
                    pygame.draw.rect(screen, (0, 0, 0), (j*carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '.':
                    pygame.draw.rect(screen, (255,255,255), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '#':
                    pygame.draw.rect(screen, (100, 100, 100), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '+':
                    pygame.draw.rect(screen, (255,100,100), (j*self.carre, i*self.carre, self.carre, self.carre))
                elif self.map_decouverte[i][j] == '-' or self.map_decouverte[i][j] == '|': 
                    pygame.draw.rect(screen, (0, 0, 255), (j*self.carre, i*self.carre, self.carre, self.carre)) 
            

