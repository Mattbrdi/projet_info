import pygame 
import Map 
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
        self.speed[0] += a[0]
        self.speed[1] += a[1]
        
    def translated_pos(self, a):
        return [self.position[0]+a[0],self.position[1] + a[1] ]
    
    def next_position(self):
        self.position = self.translated_pos(self.speed)
        
    def change_position(self, pos):
        self.position = pos
        
        
    def change_speed(self, speed):
        self.speed = speed
    
            

class personnage(objet): 
    def __init__(self, position, speed, speed_max):
        super().__init__(position, speed, speed_max)
        self.AccessibleCoordinates
    def sauter(self):
        self.speed[1]+=  speed_jump
      
    def draw(self, screen, White, x, y, radius = 30):
        pygame.draw.circle(screen, White, (x, y), radius)
    
    def def_accessible_coordinates(self, carte):
        self.AccessibleCoordinates = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] in ['.'] : #caractère access pour perso
                    for k in range(carte.carre): 
                        for l in range(carte.carre):
                            self.AccessibleCoordinates.append((j*carte.carre + k, i*carte.carre + l)) 
    
    def next_position_considering_walls(self, carte):
        while self.next_position() not in self.AccessibleCoordinates:
            if self.translated_pos([self.speed[0], 0]) not in self.AccessibleCoordinates:
                self.speed[0] -= self.speed[0]/abs(self.speed[0])
            elif self.translated_pos([0, self.speed[1]]) not in self.AccessibleCoordinates:
                self.speed[1] -= self.speed[1]/abs(self.speed[1]) 
                  
        self.position = self.next_position()  
                    
        
    def handle(self, event, en_cours, portal, portals, matsurfaces, xc, yc, dc):
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (dc[0] or dc[1]) and matsurfaces[int(yc)][int(xc)]:
            portal[portals] = ((xc, yc), matsurfaces[int(yc)][int(xc)])
            portals = 1 - portals
        return en_cours, portals, portal


        