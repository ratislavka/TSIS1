import pygame
import math

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 800))

done = False

colors = {
    "Red": (255, 0, 0),
    "White": (255, 255, 255),
    "Green": (0, 255, 0), 
    "Blue": (0, 0, 255), 
    "Black": (0, 0, 0),
    "Grey": (128, 128, 128)
}

def intersect_rect(point, rect):
    if rect[0] <= point[0] <= rect[0] + rect[2] and rect[1] <= point[1] <= rect[1] + rect[3]: return True
    else: return False
def intersect_circle(point, start, radius):
    if math.sqrt((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2) <= radius: return True
    else: return False

def Controls():
    pygame.draw.rect(screen, colors["White"], (0, 600, 600, 200))
    text = font.render("Controls:", True, colors["Black"])
    screen.blit(text, (20, 610))
    text = font.render("Colors:", True, colors["Black"])
    screen.blit(text, (20, 630))
    text = font.render("1 - Red", True, colors["Black"])
    screen.blit(text, (20, 650))
    text = font.render("2 - Green", True, colors["Black"])
    screen.blit(text, (20, 670))
    text = font.render("3 - Blue", True, colors["Black"])
    screen.blit(text, (20, 690))
    text = font.render("4 - White", True, colors["Black"])
    screen.blit(text, (20, 710))
    if mode == "Paint":
        text = font.render("LMB - increase thickness", True, colors["Black"])
        screen.blit(text, (200, 630))
        text = font.render("RMB - decrease thickness", True, colors["Black"])
        screen.blit(text, (200, 650))
    if mode == "Eraser":
        text = font.render("LMB - erase rectangle or circle", True, colors["Black"])
        screen.blit(text, (200, 630))
    if mode == "Rectangle":
        if startx == -1:
            text = font.render("LMB - choose corner point", True, colors["Black"])
            screen.blit(text, (200, 630))
        else:
            text = font.render("LMB - draw rectangle", True, colors["Black"])
            screen.blit(text, (200, 630))
    if mode == "Circle":
        if startx == -1:
            text = font.render("LMB - choose center point", True, colors["Black"])
            screen.blit(text, (200, 630))
        else:
            text = font.render("LMB - draw circle", True, colors["Black"])
            screen.blit(text, (200, 630))
    text = font.render("Q - Gradient paint", True, colors["Black"])
    screen.blit(text, (200, 670))
    text = font.render("W - Rectangle", True, colors["Black"])
    screen.blit(text, (200, 690))
    text = font.render("E - Circle", True, colors["Black"])
    screen.blit(text, (200, 710))
    text = font.render("R - Eraser", True, colors["Black"])
    screen.blit(text, (200, 730))
    text = font.render("ENTER - Exit", True, colors["Black"])
    screen.blit(text, (20, 750))

    
    if mode == "Eraser": text = font.render("You are in mode: " + mode, True, colors["Grey"])
    elif color == "White": text = font.render("You are in mode: " + mode + " (White)", True, colors["Black"])
    else: text = font.render("You are in mode: " + mode, True, colors[color])
    screen.blit(text, (200, 750))


radius = 10
mode = "Paint"
color = "Red"
points = []
rectangles = []
circles = []

font = pygame.font.Font(None, 28)
startx = -1
starty = -1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        done = True
    if pressed[pygame.K_1]:
        color = "Red"
    if pressed[pygame.K_2]:
        color = "Green"
    if pressed[pygame.K_3]:
        color = "Blue"
    if pressed[pygame.K_4]:
        color = "White"
    if pressed[pygame.K_r]:
        mode = "Eraser"
    if pressed[pygame.K_q]:
        mode = "Paint"
    if pressed[pygame.K_w]:
        mode = "Rectangle"
        startx = -1
        starty = -1
    if pressed[pygame.K_e]:
        mode = "Circle"
        startx = -1
        starty = -1
    
    m_pressed = pygame.mouse.get_pressed()
    if m_pressed[0] and mode == "Paint":
        radius += 1
        if radius > 50: radius = 50
    if m_pressed[2] and mode == "Paint":
        radius -= 1
        if radius < 1: radius = 1

    if m_pressed[0] and mode == "Rectangle":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            #rectangle (x, y, dx, dy), color
            rectangles.append(((min(pos[0], startx), min(pos[1], starty), abs(pos[0] - startx), abs(pos[1] - starty)), colors[color]))
            startx = -1
            starty = -1
    
    if m_pressed[0] and mode == "Circle":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            #center, color, radius
            circles.append(((startx, starty), colors[color], math.sqrt((pos[0] - startx) ** 2 + (pos[1] - starty) ** 2)))
            startx = -1
            starty = -1

    if m_pressed[0] and mode == "Eraser":
        pos = pygame.mouse.get_pos()
        i = 0
        while i < len(rectangles):
            if intersect_rect(pos, rectangles[i][0]):
                rectangles.pop(i)
            else: i += 1
        i = 0
        while i < len(circles):
            if intersect_circle(pos, circles[i][0], circles[i][2]):
                circles.pop(i)
            else: i += 1
    
    
    if mode == "Paint":
        pos = pygame.mouse.get_pos()
        points.insert(0, (colors[color], pos, radius))
        if len(points) > 1024: points.pop(256)
    else:
        points.insert(0, (colors[color], (-100, -100), radius))
        if len(points) > 1024: points.pop(256)

    

    screen.fill(colors["Black"])
    for i in range(len(points) - 1, -1, -1):
        cur_color = points[i][0]
        R = max(0, cur_color[0] - i)
        G = max(0, cur_color[1] - i)
        B = max(0, cur_color[2] - i)
        pygame.draw.circle(screen, (R, G, B), points[i][1], points[i][2])

    for rect in rectangles:
        pygame.draw.rect(screen, rect[1], rect[0])
    for circle in circles:
        pygame.draw.circle(screen, circle[1], circle[0], circle[2])
        
    if mode == "Rectangle":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, colors[color], (min(pos[0], startx), min(pos[1], starty), abs(pos[0] - startx), abs(pos[1] - starty)))
            
    if mode == "Circle":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, colors[color], (startx, starty), math.sqrt((pos[0] - startx) ** 2 + (pos[1] - starty) ** 2))

    if mode == "Eraser":
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, colors["Grey"], pos, 5)

    Controls()

    pygame.display.flip()
    if mode == "Paint": clock.tick(200)
    else: clock.tick(60)
    

