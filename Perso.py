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

    
        #création de sa Surface