import pygame 
#constante liés aux personnages ---------------
speed_jump = -5
#----------------------------------------------

class objet:
    def __init__(self,position, speed, speed_max):
        self.position = list(position) #liste(x,y)
        self.speed = list(speed) #liste (x,y)
        self.speed_max = list(speed_max) #liste(x,y)
        print('perso existe')
        
    def regulating_speed(self) :
        if abs(self.speed[0]) > self.speed_max[0]:
            self.speed[0] = self.speed_max[0] * self.speed[0]/ abs(self.speed[0])
        if abs(self.speed[1]) > self.speed_max[1]:
            self.speed[1] = self.speed_max[1] * self.speed[1]/ abs(self.speed[1])
            
    def acceleration(self, a):
        self.speed += a
    
    def change_position(self, pos):
        self.position = pos
        
    def next_position(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        
    def change_speed(self, speed):
        self.speed = speed
    
    @staticmethod
    def get_pos_in_carte_matrice(position, carte):#retourne l'indice de la case (ligne, colonne)
        return (position()[1]//carte.carre , position()[0]//carte.carre)
    
                    
                    
                
            

class personnage(objet): 
    def __init__(self, position, speed, speed_max):
        super().__init__(position, speed, speed_max)
           
    def sauter(self):
        self.speed[1]+=  speed_jump
        
    def draw (self, screen, White, x, y, radius = 30):
        pygame.draw.circle(screen, White, (x, y), radius)
    
    def considering_walls(self, carte):
        position = self.position
        if objet.get_pos_in_carte_matrice(position,carte) not in carte.PersoAccessibleCoordinates:
                    
        return 
    
    def handle(self, event, en_cours, portal, portals, matsurfaces, xc, yc, dc):
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (dc[0] or dc[1]) and matsurfaces[int(yc)][int(xc)]:
            portal[portals] = ((xc, yc), matsurfaces[int(yc)][int(xc)])
            portals = 1 - portals
        return en_cours, portals, portal


        