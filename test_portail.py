import pygame 

def portail_select(portail_1, portail_2, touches):
    assert portail_1.is_selected != portail_2.is_selected
    if touches[pygame.K_TAB]:
        if portail_1.is_selected:
            portail_1.is_selected = False
            portail_2.is_selected = True
        else:
            portail_1.is_selected = True
            portail_2.is_selected = False


def choose_color(color):
    if color == 'blue':
        return (0, 255, 255)
    if color == 'orange':
        return (255, 100, 0)

def get_tile_normal(grid, x, y):
    if x > 0 and grid[y][x - 1] == '.':  # There's an empty tile to the left
        return (-1, 0)
    elif x < len(grid[0]) - 1 and grid[y][x + 1] == '.':  # There's an empty tile to the right
        return (1, 0)
    elif y > 0 and grid[y - 1][x] == '.':  # There's an empty tile above
        return (0, -1)
    elif y < len(grid) - 1 and grid[y + 1][x] == '.':  # There's an empty tile below
        return (0, 1)
    else:
        return (-1, 0)  # The tile is surrounded by other tiles

def dilatation(text_file, factor):
    with open(text_file, 'r') as file:
        array = [list(line.strip().replace('@', '.')) for line in file] 
    return [[char for char in row for _ in range(factor)] for row in array for _ in range(factor)]

#Correction du placement du portail en fonction de l'orientation de ce dernier
pos = {'up':     [-29, 25 , 60, 14], 
       'down':   [-29, -38, 60, 14], 
       'left':   [25, -28, 14, 60], 
        'right': [-38, -28, 14, 60],
      }
 
class Portail: 
    def __init__(self, screen, carte, color):
        self.x = 0 
        self.y = 0 
        self.screen = screen 
        self.map = dilatation(carte, 32)
        self.color = color 
        self.drawing_color = choose_color(self.color)
        self.facing = 'none'
        self.is_selected = False 
        self.is_placed = False
    
    #TODO : the int position may not be the position of the character
    def get_draw_position(self, touches, position):
        int_position = [int(position[0]),int(position[1])]
        i = int_position[1]
        j = int_position[0]
        max_i = len(self.map) - 1
        max_j = len(self.map[0]) - 1
        #print(i , j)
        if touches[pygame.K_z] and not touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_s]:
            #print(i,j,  len(self.map), len(self.map[0]))
            while self.map[i][j] == '.' and i >= 0:
                #print(self.map[i][j])
                i -= 1
        elif touches[pygame.K_s] and not touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_z]:
            while self.map[i][j] == '.' and i <= max_i:
                i += 1
        elif touches[pygame.K_q] and not touches[pygame.K_z] and not touches[pygame.K_s] and not touches[pygame.K_d]:
            while self.map[i][j] == '.' and j >= 0:
                j -= 1
        elif touches[pygame.K_d] and not touches[pygame.K_z] and not touches[pygame.K_s] and not touches[pygame.K_q]:
            while self.map[i][j] == '.' and j <= max_j:
                j += 1
        elif touches[pygame.K_z] and touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_s]:
            while self.map[i][j] == '.' and i >= 0 and j >= 0:
                i -= 1
                j -= 1
        elif touches[pygame.K_z] and touches[pygame.K_d] and not touches[pygame.K_q] and not touches[pygame.K_s]:
            while self.map[i][j] == '.' and i >= 0 and j <= max_j:
                i -= 1
                j += 1
        elif touches[pygame.K_s] and touches[pygame.K_q] and not touches[pygame.K_d] and not touches[pygame.K_z]:
            while self.map[i][j] == '.' and i <= max_i and j >= 0:
                i += 1
                j -= 1
        elif touches[pygame.K_s] and touches[pygame.K_d] and not touches[pygame.K_q] and not touches[pygame.K_z]:
            while self.map[i][j] == '.' and i <= max_i and j <= max_j:
                i += 1
                j += 1
        return j, i
    
    def get_portal_facing(self, surface_normal):
        if surface_normal == (0, -1):  
            return 'up'
        elif surface_normal == (0, 1):  
            return 'down'
        elif surface_normal == (-1, 0):  
            return 'left'
        elif surface_normal == (1, 0):
            return 'right'
        else:
            return 'none'  # Surface normal doesn't match any known direction

    def draw(self, screen, position, touches):
        if self.is_selected:
            if touches[pygame.K_SPACE]:
                self.x, self.y = self.get_draw_position(touches, position)
                self.facing = self.get_portal_facing(get_tile_normal(self.map, self.x, self.y))
                if touches[pygame.K_z] or touches[pygame.K_s] or touches[pygame.K_q] or touches[pygame.K_d]:
                    self.is_placed = True
                    self.keep_drawing(screen)
                    
    def keep_drawing(self, screen):
        rect_ovale = pygame.Rect(self.x + pos[self.facing][0], self.y + pos[self.facing][1], pos[self.facing][2], pos[self.facing][3])
        pygame.draw.ellipse(screen, self.drawing_color, rect_ovale)

    
        
