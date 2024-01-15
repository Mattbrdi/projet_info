import pygame
import random as rd

#inventaire des constante
accel_saut_perso = 5


class Personnage:
    def __init__(self,pos_x,pos_y,v_x,v_y,vmax_x,vmax_y):
        self.pos_x = pos_x #position initiale
        self.pos_y = pos_y #on distingue x et y pour clarifié et eviter soucis de modif dans une fct 
        self.v_x = v_x #comme vu en cours
        self.v_y = v_y
        self.vmax_x = vmax_x
        self.vmax_y = vmax_y
        print('perso existe')
        
    def acceleration_x(self, v):
        if self.v_x < self.vmax_x -v:
            self.v_x += v
        elif self.v_x < self.vmax_x:
            self.v_x = self.vmax_x
            
    def acceleration_y(self, v):
        if self.v_y < self.vmax_y -v:
            self.v_y += v
        elif self.v_y < self.vmax_y:
            self.v_y = self.vmax_y
    
    def sauter(self):
        self.acceleration_y(accel_saut_perso) #valeur à modifier en fonction de la dynamique du jeu 

            
    class Map:
        def __init__(self, matrice, dim_x, dim_y, spawn_x, spawn_y):
            self.matrice = matrice #matrice représentative de la map
            self.dim_x = dim_x #nombre de pixel de largeur
            self.dim_y = dim_y
        
        def Surface_map(self):
            
