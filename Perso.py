#constante liés aux personnages ---------------
vitesse_saut = 5
#----------------------------------------------

class objet:
    def __init__(self,position, speed, speed_max,):
        self.position = position #tuple(x,y)
        self.speed = speed #tuple(x,y)
        self.speed_max = speed_max #tuple(x,y)
        print('perso existe')
        
    def regulating_speed(self) :
        if 
    def acceleration_x(self, a):
        self.speed
        
        
            
    def changement_speed(self, speed):
        self.speed = speed

class personnage(objet): 
    def __init__(self, position, speed, speed_max):
        super().__init__(position, speed, speed_max)
        
    def sauter(self):
        self.speed[1]+=  speed_saut
        
    def draw (self, screen, White, x, y, radius = 30):
        pygame.draw.circle(screen, White, (x, y), radius)
    
    def handle(self, event, en_cours, portal, portals, matsurfaces, xc, yc, dc):
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (dc[0] or dc[1]) and matsurfaces[int(yc)][int(xc)]:
            portal[portals] = ((xc, yc), matsurfaces[int(yc)][int(xc)])
            portals = 1 - portals
        return en_cours, portals, portal


        