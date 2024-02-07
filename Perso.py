import pygame 
import Map 
#constante liés aux personnages ---------------
speed_jump = -5
gravite = 1
accel =1
speed_max = [3, 10]
taille_personnage = 30
couleur_perso = (255,0,0)
#----------------------------------------------

class objet:
    def __init__(self,position, speed_max = speed_max):
        self.position = list(position) #liste(x,y)
        self.speed = [0,0] #liste (x,y)
        self.speed_max = list(speed_max) #liste(x,y)
        print('perso existe')
        
            
    def acceleration(self, a):
        if abs(self.speed[0] + a[0]) <= self.speed_max[0] :
            self.speed[0] += a[0]
        elif abs(self.speed[0]) <= self.speed_max[0] :
            self.speed[0]= self.speed_max[0]*a[0]/abs(a[0])
        if abs(self.speed[1] + a[1]) <= self.speed_max[1]:
            self.speed[1] += a[1]
        elif abs(self.speed[1]) <= self.speed_max[1] :
            self.speed[1]= self.speed_max[1] *a[1]/abs(a[1])
        
    def translated_pos(self, a):
        return [self.position[0]+a[0],self.position[1] + a[1] ]
    
    def next_position(self):
        return self.translated_pos(self.speed)
        
    def change_position(self, pos):
        self.position = pos   
        
    def change_speed(self, speed):
        self.speed = speed
    
            

class personnage(objet): 
    def __init__(self, position, speed_max = speed_max):
        super().__init__(position, speed_max)
        self.AccessibleCoordinates = []
      
    def draw(self, screen):
        pygame.draw.circle(screen, couleur_perso, self.position, taille_personnage)
    
    def def_accessible_coordinates(self, carte):
        self.AccessibleCoordinates = []
        for i in range(len(carte.map)):
            for j in range(len(carte.map[i])):
                if carte.map[i][j] in ['.', '@'] : #caractère access pour perso
                    for k in range(carte.carre): 
                        for l in range(carte.carre):
                            self.AccessibleCoordinates.append((j*carte.carre + k, i*carte.carre + l)) 
        
    def next_position_considering_walls(self):
        print(self.position)
        print(self.next_position())
        print(self.next_position not in self.AccessibleCoordinates)
        while self.next_position() not in self.AccessibleCoordinates:
            if self.translated_pos([self.speed[0], 0]) not in self.AccessibleCoordinates:
                self.speed[0] -= self.speed[0]/abs(self.speed[0])
            elif self.translated_pos([0, self.speed[1]]) not in self.AccessibleCoordinates:
                self.speed[1] -= self.speed[1]/abs(self.speed[1]) 
                
        self.position = self.next_position()  
                    
    def jump(self):
        if self.translated_pos([0,1]) not in self.AccessibleCoordinates:
            self.speed[1]=  speed_jump
            
    def handle_event(self, event)   :
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.acceleration([-accel,0])
            elif event.key == pygame.K_RIGHT:
                self.acceleration([accel,0])
            elif event.key == pygame.K_UP:
                self.jump()
                
    def gravite(self):
        self.acceleration([0,gravite])
        
    def handle(self, event, en_cours, portal, portals, matsurfaces, xc, yc, dc):
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (dc[0] or dc[1]) and matsurfaces[int(yc)][int(xc)]:
            portal[portals] = ((xc, yc), matsurfaces[int(yc)][int(xc)])
            portals = 1 - portals
        return en_cours, portals, portal


    def update(self):
        self.gravite()
        self.next_position_considering_walls()