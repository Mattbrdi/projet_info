import pygame
import random as rd
import Mattis as matt


pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()


#création de la carte : methode numéro 1
White = (255, 255, 255)
sol1 = [(i, 410) for i in range(101)]
sol2 = [(250 + i, 410) for i in range(471)]
sol3 = [(100 + i, 180) for i in range(151)]
sols = [sol1, sol2, sol3]
plafond1 = [(100 + i, 220) for i in range(151)]
plafonds = [plafond1]
paroiL1 = [(100, 410 + i) for i in range(311)]
paroiL2 = [(250, 180 + i) for i in range(41)]
paroisL = [paroiL1, paroiL2]
paroiR1 = [(250, 410 + i) for i in range(311)]
paroiR2 = [(100, 180 + i) for i in range(41)]
paroisR = [paroiR1, paroiR2]
surfaces = paroisR + paroisL + plafonds + sols
matsurfaces = [[0 for i in range(721)] for j in range(721)]

for sol in sols:
    for x, y in sol:
        matsurfaces[y][x] = 1

for plafond in plafonds:
    for x, y in plafond:
        matsurfaces[y][x] = 3

for paroi in paroisR:
    for x, y in paroi:
        matsurfaces[y][x] = 2

for paroi in paroisL:
    for x, y in paroi:
        matsurfaces[y][x] = 4

def collision(point, surface):
    for x, y in surface:
        if (point[0] - x)**2 + (point[1] - y)**2 <= 30**2:
            return True
    return False


#définition des paramètres du perso : idée numéro 1

x = 360
y = 360
xc = 0
yc = 0
vx = 0
vy = 0
ay = -0.01
color = (0, 255, 255)

en_cours = True
portal = {}
portals = 0
plaf = False
perso = matt.Personnage(x, y, vx, vy)# vmax_x, vmax_y)

#jeu qui tourne 
while en_cours:
    clock.tick(800)
    touches = pygame.key.get_pressed()
    if perso.pos_y > 720:
        perso.pos_y = 0
    if perso.pos_y < 0:
        perso.pos_y = 720
    if perso.pos_x > 720:
        perso.pos_x = 0
    if perso.pos_x < 0:
        perso.pos_x = 720
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, (0, 410, 720, 310))
    pygame.draw.rect(screen, color, (100, 180, 150, 40))
    pygame.draw.rect(screen, (0, 0, 0), (100, 410, 150, 310))
    perso.draw(screen, White, perso.pos_x, perso.pos_y, 30)
    #pygame.draw.circle(screen, White, (x, y), 30)
    dc = [0, 0] 
    if touches[pygame.K_d]:
        dc[0] += 1
    if touches[pygame.K_s]:
        dc[1] += 1 
    if touches[pygame.K_q]:
        dc[0] += -1
    if touches[pygame.K_z]:
        dc[1] += -1
    if dc[0] or dc[1]:
        xc, yc = perso.pos_x, perso.pos_y
        while 0 < xc < 720 and 0 < yc < 720 and not matsurfaces[int(yc)][int(xc)]:
            xc += dc[0]
            yc += dc[1]
        pygame.draw.line(screen, (255, 0, 0), (perso.pos_x, perso.pos_y),(xc, yc), 3)
    for event in pygame.event.get():
        en_cours, portals, portal = perso.handle(event, en_cours, portal, portals, matsurfaces, xc, yc, dc)
        # if event.type == pygame.QUIT:
        #     en_cours = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (dc[0] or dc[1]) and matsurfaces[int(yc)][int(xc)]:
        #     portal[portals] = ((xc, yc), matsurfaces[int(yc)][int(xc)])
        #     portals = 1 - portals
    for key in portal:
        if portal[key][1] % 2 == 1:
            rect_ovale = pygame.Rect(portal[key][0][0] - 30, portal[key][0][1] - 7, 60, 14)
        if portal[key][1] % 2 == 0:
            rect_ovale = pygame.Rect(portal[key][0][0] - 7, portal[key][0][1] - 30, 14, 60)
        pygame.draw.ellipse(screen, (255*(1-key), 100*(1-key), 255*key), rect_ovale)
    if collision((perso.pos_x, perso.pos_y), plafond1) and not plaf:
        vy = 0
        plaf = True
    vy += ay
    state = sum(collision((perso.pos_x, perso.pos_y), sol) for sol in sols)
    if state:
        vy = 0
        plaf = False
        vx = 0
    if touches[pygame.K_RIGHT] and not sum(collision((perso.pos_x, perso.pos_y), paroi) for paroi in paroisR) and vx <= 0.8:
        vx = 0.8
    if touches[pygame.K_LEFT] and not sum(collision((perso.pos_x, perso.pos_y), paroi) for paroi in paroisL) and vx >= - 0.8:
        vx = - 0.8
    if sum(collision((perso.pos_x, perso.pos_y), paroi) for paroi in paroisL):
        vx = 0
        perso.pos_x += 0.3
    if sum(collision((perso.pos_x, perso.pos_y), paroi) for paroi in paroisR):
        vx = 0
        perso.pos_x -= 0.3
    if touches[pygame.K_UP] and state:
        vy = 2
    for key in portal:
        if (portal[key][0][0] - perso.pos_x)**2 + (portal[key][0][1] - perso.pos_y)**2 <= 32**2 and len(portal) == 2:
            m = matsurfaces[int(portal[1 - key][0][1])][int(portal[1 - key][0][0])]
            if  m % 2 == 1:
                perso.pos_y = portal[1 - key][0][1] + (m-2)*40
                perso.pos_x = portal[1 - key][0][0]
                vy = (2-m)*2
            if m % 2 == 0:
                perso.pos_y = portal[1 - key][0][1]
                perso.pos_x = portal[1 - key][0][0] + (m-3)*40
                vx = (m-3)*1
    perso.pos_y -= vy
    perso.pos_x += vx
    pygame.display.update()
        
pygame.quit()
