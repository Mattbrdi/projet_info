import pygame
import random as rd
          
class Map:
    def __init__(self, matrice,dimension, spawn):
        self.matrice = matrice #matrice représentative de la map
        self.dimension = dimension
        self.spawn = spawn
        

            
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock() 