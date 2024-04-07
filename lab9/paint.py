import pygame
import sys
import math
pygame.init()

height = 600
panel_height = 100
width = 800

window = pygame.display.set_mode((width, height))
screen = pygame.Surface((width, height - panel_height))
another_layer = pygame.Surface((width, height - panel_height))
panel = pygame.Surface((width, panel_height))

queue = []

def getRectangle(x1, y1, x2, y2):
        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x1-x2)
        h = abs(y1-y2)
        return (x, y, w, h)

def getCircle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    return (x, y)

def getRadius(x1, y1, x2, y2):
    r = max(abs(x1-x2), abs(y1-y2))
    return r

def step(screen, x, y, origin_color, fill_color):
    if x < 0 or y < 0: return False
    if x > width-1 or y > height-panel_height-1: return False
    if screen.get_at((x, y)) != origin_color: return False
    queue.append((x, y))
    screen.set_at((x, y), fill_color)

pencil = pygame.image.load('photo_5230987540956307075_x.jpg')
pencil = pygame.transform.scale(pencil, (75, 75))
rect = pencil.get_rect()
rect1 = rect.move(10, 10)
rect2 = rect.move(95, 10)
rect3 = rect.move(180, 10)
rect4 = rect.move(265, 10)

bucket = pygame.image.load('photo_5230987540956307071_m.jpg')
bucket = pygame.transform.scale(bucket, (75, 75))

eraser = pygame.image.load('photo_5230987540956307070_m.jpg')
eraser = pygame.transform.scale(eraser, (75, 75))

figures = pygame.image.load('photo_5230987540956307076_m.jpg')
figures = pygame.transform.scale(figures, (75, 75))

rectangle = pygame.image.load('photo_5230987540956307073_m.jpg')
rectangle = pygame.transform.scale(rectangle, (75, 95))

circle = pygame.image.load('photo_5230987540956307077_y.jpg')
circle = pygame.transform.scale(circle, (75, 75))

pallete = pygame.image.load('photo_5230987540956307078_y.jpg')
pallete = pygame.transform.scale(pallete, (75, 75))

BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)
VIOLETE = (128, 0, 128)
forest_green = ((0,50,0))
magenta = ((255,0,230))
pink = ((255,100,180))

COLOR = WHITE

mouse_pressed = False

tool = 0
tools = 4

screen.fill(BLACK)

poligons = False
color_changing = False

while True:
    
    fill_color = COLOR
    panel.fill(DARK_GRAY)
    if poligons:
        panel.blit(rectangle, (10, 10))
        panel.blit(circle, (95, 10))
        panel.blit(rectangle, (180, 10))
        panel.blit(circle, (260,10))
        panel.blit(rectangle, (345, 10))
        panel.blit(circle, (430,10))
        if tool == 1:
            pygame.draw.rect(panel, BLUE, rect1, 1)
        if tool == 4:
            pygame.draw.rect(panel, BLUE, rect2, 1)
    elif color_changing:
       pygame.draw.circle(panel, BLUE, (40,50),30)
       pygame.draw.circle(panel, RED, (120,50),30)
       pygame.draw.circle(panel, GREEN, (200,50),30)
       pygame.draw.circle(panel, WHITE, (280,50),30)
       pygame.draw.circle(panel, YELLOW, (360,50),30)
       pygame.draw.circle(panel, ORANGE, (440,50),30)
       pygame.draw.circle(panel, VIOLETE, (520,50),30)
       pygame.draw.circle(panel, forest_green, (600,50),30)
       pygame.draw.circle(panel, magenta, (680,50),30)
       pygame.draw.circle(panel, pink, (760,50),30)
    else:
        panel.blit(pencil, (10, 10))
        panel.blit(bucket, (95, 10))
        panel.blit(eraser, (180, 10))
        panel.blit(figures, (265, 10))
        panel.blit(pallete, (605, 10))
        pygame.draw.circle(panel, COLOR,(440,50), 35)
        pygame.draw.circle(panel, BLACK,(440,50), 35, 3)
        if tool == 0:
            pygame.draw.rect(panel, BLUE, rect1, 1)
        elif tool == 2:
            pygame.draw.rect(panel, BLUE, rect2, 1)
        elif tool == 3:
            pygame.draw.rect(panel, BLUE, rect3, 1)
        else:
            pygame.draw.rect(panel, BLUE, rect4, 1)
        
    pos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                x1 = pos[0]
                y1 = pos[1] - panel_height
                if tool == 0:
                    x2 = x1
                    y2 = y1
                elif tool == 2:
                    if pos[1] >= 100:
                        origin_color = screen.get_at((x1, y1))
                        if origin_color != fill_color:
                            queue.append((x1, y1))
                            screen.set_at((x1, y1), fill_color)

                            while len(queue):
                                cur_pos = queue[0]
                                queue.pop(0)
                                step(screen, cur_pos[0] + 1, cur_pos[1], origin_color,  fill_color)
                                step(screen, cur_pos[0] - 1, cur_pos[1], origin_color,  fill_color)
                                step(screen, cur_pos[0], cur_pos[1] + 1, origin_color,  fill_color)
                                step(screen, cur_pos[0], cur_pos[1] - 1, origin_color,  fill_color)
                if tool == 3:
                    pygame.draw.rect(screen, BLACK, (x1-25, y1-25, 50, 50), border_radius=10)
                mouse_pressed = True
                if pos[1] < 100:
                    if poligons:
                        if 10 < pos[0] and pos[0] < 90:
                            tool = 1
                        elif 95 < pos[0] and pos[0] < 175:
                            tool = 4
                        elif 180 < pos[0] and pos[0] < 260:
                            tool = 5
                        elif 265 < pos[0] and pos[0] < 345:
                            tool = 6
                        elif 350 < pos[0] and pos[0] < 430:
                            tool = 7
                        elif 435 < pos[0] and pos[0] <515:
                            tool = 8
                    elif color_changing:
                        if 40-30 < pos[0] and pos[0] < 40+30:
                            COLOR = BLUE
                        elif 120-30 < pos[0] and pos[0] < 120+30:
                            COLOR = RED
                        elif 200-30 < pos[0] and pos[0] < 200+30:
                            COLOR = GREEN 
                        elif 280-30 < pos[0] and pos[0] < 280+30:
                            COLOR = WHITE 
                        elif 360-30 < pos[0] and pos[0] < 360+30:
                            COLOR = YELLOW 
                        elif 440-30 < pos[0] and pos[0] < 440+30:
                            COLOR = ORANGE 
                        elif 520-30 < pos[0] and pos[0] < 520+30:
                            COLOR = VIOLETE
                        elif 600-30 < pos[0] and pos[0] < 600+30:
                            COLOR = forest_green
                        elif 680-30 < pos[0] and pos[0] < 680+30:
                            COLOR = magenta 
                        elif 760-30 < pos[0] and pos[0] < 760+30:
                            COLOR = pink
                    else:
                        if 10 < pos[0] and pos[0] < 90:
                            tool = 0
                        elif 95 < pos[0] and pos[0] < 175:
                            tool = 2
                        elif 180 < pos[0] and pos[0] < 260:
                            tool = 3
                        elif 265 < pos[0] and pos[0] < 345:
                            poligons = True
                        elif 605 < pos[0] and pos[0] < 685:
                            color_changing = True
                else:
                    poligons = False
                    color_changing = False
                    
        if e.type == pygame.MOUSEBUTTONUP:
            another_layer.blit(screen, (0, 0))
            mouse_pressed = False

        if e.type == pygame.MOUSEMOTION:
            if mouse_pressed:
                if tool == 0:
                    x1 = x2
                    y1 = y2
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.line(screen, COLOR, (x1, y1), (x2, y2))
                elif tool == 1:
                    screen.blit(another_layer, (0, 0))
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.rect(screen, COLOR, pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                elif tool == 4:
                    screen.blit(another_layer, (0, 0))
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.circle(screen, COLOR,  (getCircle(x1, y1, x2, y2)), getRadius(x1, y1, x2, y2), 2)
                elif tool == 3:
                    x2 = pos[0]
                    y2 = pos[1] - 100
                    pygame.draw.rect(screen, BLACK, (x2-25, y2-25, 50, 50), border_radius=10)
                elif tool == 5:
                    screen.blit(another_layer, (0, 0))
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.polygon(screen, COLOR,[(x1+50, y2),(x1, y1), (x1-50, y2), (x1, 2*y2-y1)], 1)
                elif tool == 6:
                    screen.blit(another_layer, (0, 0))
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.polygon(screen, COLOR,[(x1, y1),(x1, y2), (x2, y1)], 1)
                elif tool == 7:
                    screen.blit(another_layer, (0, 0))
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.polygon(screen, COLOR,[(x1, y1),(x2, y1), ((x1+x2)/2, y1-(abs(x1-x2))*math.sqrt(3)/2)], 1)
                elif tool == 8:
                    screen.blit(another_layer, (0, 0))
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.polygon(screen, COLOR,[(x1, y1),(x1,y1 - abs(x1-x2)),(x2,y1 - abs(x1-x2)),(x2, y1)], 1)
    window.blit(panel, (0, 0))
    window.blit(screen, (0, 100))
    pygame.display.update()