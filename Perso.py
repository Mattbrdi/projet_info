import pygame 
import Map 
#constante liés aux personnages --------------- influe sur la dynamique du jeu

speed_jump = -13
gravite = 1
accel =5
speed_max = [accel, 5*accel]
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
        self.taille_personnage = 0
        
    def draw(self, screen):
        points_losange = []
        i_j = [(1,1), (-1,1), (-1,-1), (1,-1)]
        for i, j in i_j   :
            points_losange.append((self.position[0] +i*self.taille_personnage, self.position[1]+ j*self.taille_personnage))
        pygame.draw.polygon(screen, couleur_perso, points_losange)
        #pygame.draw.circle(screen, couleur_perso, self.position, self.taille_personnage)
    #adaptation du perso à la map
    def def_accessible_coordinates(self, carte):
        self.AccessibleCoordinates = []
        for i in range(len(carte.map)):
            for j in range(len(carte.map[i])):
                if carte.map[i][j] in ['.', '@'] :#caractère access pour perso
                    for k in range(carte.carre): 
                        for l in range(carte.carre):
                            self.AccessibleCoordinates.append([j*carte.carre + k, i*carte.carre + l]) 
    def size(self, carte):
        self.taille_personnage = carte.carre
    
    def regle_a_la_map(self, carte):
        self.def_accessible_coordinates(carte)
        self.size(carte)
          
#déplacement du perso acceleration   
    def is_on_the_ground(self):
        return self.translated_pos([0,1]) not in self.AccessibleCoordinates
    
    def jump(self):
        if self.is_on_the_ground() :
            self.speed[1]=  speed_jump
            
    def handle_key_pressed(self, touches, portail):
        if touches[pygame.K_LEFT]:
            self.acceleration([-accel,0])
        if touches[pygame.K_RIGHT]:
            self.acceleration([accel,0])
        if touches[pygame.K_UP]:
            self.jump()
        if touches[pygame.K_z] or touches[pygame.K_s] or touches[pygame.K_q] or touches[pygame.K_d]:
            portail.get_draw_position(touches, self.position)
            
    def gravite(self):
        self.acceleration([0,gravite])
    
    def frottement(self):
        if self.is_on_the_ground():
            self.acceleration([-self.speed[0],0])
            
    def force_applicated(self):
        self.gravite()
        self.frottement()
        
    #application des acceleration : deplacement réel du perso
    def next_position_considering_walls(self):
        while self.next_position() not in self.AccessibleCoordinates :
            if self.translated_pos([self.speed[0], 0]) not in self.AccessibleCoordinates and self.speed[0] != 0:
                self.speed[0] -= self.speed[0]/abs(self.speed[0])
            elif self.translated_pos([0, self.speed[1]]) not in self.AccessibleCoordinates and self.speed[1] != 0:
                self.speed[1] -= self.speed[1]/abs(self.speed[1]) 
            elif self.speed[0] != 0 and self.speed[1] != 0:  
                self.speed[0] -= self.speed[0]/abs(self.speed[0])
                self.speed[1] -= self.speed[1]/abs(self.speed[1]) 

        self.position = self.next_position()

        
        
        



#pas compris à quoi ca sert
    def handle(self, event, en_cours, portal, portals, matsurfaces, xc, yc, dc):
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (dc[0] or dc[1]) and matsurfaces[int(yc)][int(xc)]:
            portal[portals] = ((xc, yc), matsurfaces[int(yc)][int(xc)])
            portals = 1 - portals
        return en_cours, portals, portal
    
    def teleportation(self, carte, portail_blue, portail_orange):
            if (self.position[0] - portail_blue.x)**2 + (self.position[1] - portail_blue.y)**2 <= (carte.carre + 10)**2 and (portail_blue.is_placed and portail_orange.is_placed):
                if portail_orange.facing == 'right':
                    self.position = [portail_orange.x + 2*carte.carre, portail_orange.y]
                    if portail_blue.facing == 'left':
                        self.change_speed([-self.speed[0], -self.speed[1]]) 
                    if portail_blue.facing == 'up':
                        self.change_speed([self.speed[1], -self.speed[0]]) 
                    if portail_blue.facing == 'down':
                        self.change_speed([-self.speed[1], self.speed[0]]) 

                elif portail_orange.facing == 'left':
                    self.position = [portail_orange.x - 2*carte.carre, portail_orange.y]
                    if portail_blue.facing == 'right':
                        self.change_speed([-self.speed[0], -self.speed[1]]) 
                    if portail_blue.facing == 'up':
                        self.change_speed([-self.speed[1], self.speed[0]]) 
                    if portail_blue.facing == 'down':
                        self.change_speed([self.speed[1], -self.speed[0]]) 

                elif portail_orange.facing == 'up':
                    self.position = [portail_orange.x, portail_orange.y - 2*carte.carre]
                    if portail_blue.facing == 'right':
                        self.change_speed([-self.speed[1], self.speed[0]]) 
                    if portail_blue.facing == 'left':
                        self.change_speed([self.speed[1], -self.speed[0]]) 
                    if portail_blue.facing == 'down':
                        self.change_speed([-self.speed[0], -self.speed[1]]) 

                elif portail_orange.facing == 'down':
                    self.position = [portail_orange.x, portail_orange.y + 2*carte.carre]
                    if portail_blue.facing == 'right':
                        self.change_speed([self.speed[1], -self.speed[0]]) 
                    if portail_blue.facing == 'left':
                        self.change_speed([-self.speed[1], self.speed[0]]) 
                    if portail_blue.facing == 'up':
                        self.change_speed([-self.speed[0], -self.speed[1]]) 
                    

            elif (self.position[0] - portail_orange.x)**2 + (self.position[1] - portail_orange.y)**2 <= (carte.carre + 10)**2 and (portail_blue.is_placed and portail_orange.is_placed):
                if portail_blue.facing == 'right':
                    self.position = [portail_blue.x + 2*carte.carre, portail_blue.y]
                    if portail_orange.facing == 'left':
                        self.change_speed([-self.speed[0], -self.speed[1]]) 
                    if portail_orange.facing == 'up':
                        self.change_speed([self.speed[1], -self.speed[0]]) 
                    if portail_orange.facing == 'down':
                        self.change_speed([-self.speed[1], self.speed[0]]) 

                elif portail_blue.facing == 'left':
                    self.position = [portail_blue.x - 2*carte.carre, portail_blue.y]
                    if portail_orange.facing == 'right':
                        self.change_speed([-self.speed[0], -self.speed[1]]) 
                    if portail_orange.facing == 'up':
                        self.change_speed([-self.speed[1], self.speed[0]]) 
                    if portail_orange.facing == 'down':
                        self.change_speed([self.speed[1], -self.speed[0]]) 
                    
                elif portail_blue.facing == 'up':
                    self.position = [portail_blue.x, portail_blue.y - 2*carte.carre]
                    if portail_orange.facing == 'right':
                        self.change_speed([-self.speed[1], self.speed[0]]) 
                    if portail_orange.facing == 'left':
                        self.change_speed([self.speed[1], -self.speed[0]]) 
                    if portail_orange.facing == 'down':
                        self.change_speed([-self.speed[0], -self.speed[1]]) 

                elif portail_blue.facing == 'down':
                    self.position = [portail_blue.x, portail_blue.y + 2*carte.carre]
                    if portail_orange.facing == 'right':
                        self.change_speed([self.speed[1], -self.speed[0]]) 
                    if portail_orange.facing == 'left':
                        self.change_speed([-self.speed[1], self.speed[0]]) 
                    if portail_orange.facing == 'up':
                        self.change_speed([-self.speed[0], -self.speed[1]])
    
    
    