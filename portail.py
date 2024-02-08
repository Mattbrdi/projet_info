import pygame 

class Portail:
    def __init__(self, screen, carte, x1 = 0 , y1 = 0 , x2 = 0 , y2 = 0):
        self.x_blue = x1
        self.y_blue = y1
        self.x_orange = x2
        self.y_orange = y2
        self.is_blue = False
        self.is_orange = False
        self.screen = screen
        self.blue = (0, 255, 255)
        self.orange = (255, 100, 0)
        self.map = carte.map
        self.selected_portal = 'orange'
        self.facing = 'right'
    
    def portail_select(self, touches):
        if touches[pygame.K_TAB]:
            if self.selected_portal == 'blue':
                self.selected_portal = 'orange'
            else:
                self.selected_portal = 'blue'

    '''
    def get_facing(self):
        carte = self.map
        i, j = self.y_blue // 32, self.x_blue // 32
        if carte[i][j-1] != '.':
            self.facing = 'right'
    '''

    def get_draw_position(self, touches, position):
        int_position = [int(position[0]),int(position[1])]

        if touches[pygame.K_z] and not touches[pygame.K_q] and not touches[pygame.K_d]:
            i = int_position[1]
            while self.map[i // 32 ][int_position[0] // 32 ] == '.':
                i -= 1
                print(int_position[0], i )
            self.facing = 'up'
            return int_position[0], i - 8
        
        if touches[pygame.K_s] and not touches[pygame.K_q] and not touches[pygame.K_d]:
            i = int_position[1]
            while self.map[i // 32 ][int_position[0] // 32 ] == '.':
                i += 1
            self.facing = 'down'
            return int_position[0], i+16
        
        if touches[pygame.K_q] and not touches[pygame.K_z] and not touches[pygame.K_s] and not touches[pygame.K_d]:
            i = int_position[0]
            while self.map[int_position[1] // 32 ][i // 32 ] == '.':
                i -= 1
            self.facing = 'left'
            return i - 16 , int_position[1]
        
        if touches[pygame.K_d] and not touches[pygame.K_z] and not touches[pygame.K_s] and not touches[pygame.K_q]:
            i = int_position[0]
            while self.map[int_position[1] // 32 ][i // 32 ] == '.':
                i += 1
            self.facing = 'right'
            return i + 16 , int_position[1]
        
        if touches[pygame.K_z] and touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_s]:
            i = int_position[1]
            j = int_position[0]
            while self.map[i // 32 ][j // 32 ] == '.':
                i -= 1
                j -= 1
            self.facing = 'left'
            return j - 16 , i
        
        if touches[pygame.K_z] and touches[pygame.K_d] and not touches[pygame.K_q] and not touches[pygame.K_s]:
            i = int_position[1]
            j = int_position[0]
            while self.map[i // 32 ][j // 32 ] == '.':
                i -= 1
                j += 1
            self.facing = 'right'
            return j + 16 , i
        
        if touches[pygame.K_s] and touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_z]:
            i = int_position[1]
            j = int_position[0]
            while self.map[i // 32 ][j // 32 ] == '.':
                i += 1
                j -= 1
            self.facing = 'left'
            return j - 16, i
        
        if touches[pygame.K_s] and touches[pygame.K_d] and not touches[pygame.K_q] and not touches[pygame.K_z]:
            i = int_position[1]
            j = int_position[0]
            while self.map[i // 32 ][j // 32 ] == '.':
                i += 1
                j += 1
            self.facing = 'right'
            return j + 16, i


#TODO: add the other cases
    def draw_blue(self, screen):
        if self.facing == 'left' or 'right':
            rect_ovale = pygame.Rect(self.x_blue - 7, self.y_blue - 30, 14, 60)
            pygame.draw.ellipse(screen, self.blue, rect_ovale)
        else:
            rect_ovale = pygame.Rect(self.x_blue - 7, self.y_blue - 30, 60, 14)
            pygame.draw.ellipse(screen, self.blue, rect_ovale)

        pygame.display.flip()
        self.is_blue = True
    
    def draw_orange(self, screen):
        if self.facing == 'left' or 'right':
            rect_ovale = pygame.Rect(self.x_orange - 7, self.y_orange - 30, 14, 60)
            pygame.draw.ellipse(screen, self.orange, rect_ovale)
        if self.facing == 'up' or 'down':
            rect_ovale = pygame.Rect(self.x_orange - 7, self.y_orange - 30, 60, 14)
            pygame.draw.ellipse(screen, self.orange, rect_ovale)
        pygame.display.flip()
        self.is_orange = True

    def remove_blue(self, screen):
        if self.is_blue:
            rect_ovale = pygame.Rect(self.x_blue - 7, self.y_blue - 30, 14, 60)
            pygame.draw.ellipse(screen, self.blue, rect_ovale)
            self.is_blue = False
    
    def remove_orange(self, screen):
        if self.is_orange:
            rect_ovale = pygame.Rect(self.x_orange - 7, self.y_orange - 30, 14, 60)
            pygame.draw.ellipse(screen, self.orange, rect_ovale)
            self.is_orange = False
    
    def draw(self, screen, position, touches):
        if touches[pygame.K_SPACE]:
            if self.selected_portal == 'blue':
                if touches[pygame.K_z] or touches[pygame.K_s] or touches[pygame.K_q] or touches[pygame.K_d]:
                    self.remove_blue(screen)
                    self.x_blue, self.y_blue = self.get_draw_position(touches, position)
                    self.draw_blue(screen)
                    print('blue drawn')
            else:
                if touches[pygame.K_z] or touches[pygame.K_s] or touches[pygame.K_q] or touches[pygame.K_d]:
                    self.remove_orange(screen)
                    self.x_orange, self.y_orange = self.get_draw_position(touches, position)
                    self.draw_orange(screen)

    def keep_drawing(self, screen):
        if self.is_blue:
            self.draw_blue(screen)
        if self.is_orange:
            self.draw_orange(screen)
   

    def teleportation(self, position):
        if self.x_blue == position[0] and self.y_blue == position[1] and self.is_orange: 
            return [self.x_orange, self.y_orange]
        if self.x_orange == position[0] and self.y_orange == position[1] and self.is_blue:
            return [self.x_blue, self.y_blue]
    
