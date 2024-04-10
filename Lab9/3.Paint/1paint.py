import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing = False
    shape = 'line'
    start_pos = None
    circles = []  # Add this line to keep track of the circles

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_s:
                    shape = 'square'
                elif event.key == pygame.K_l:
                    shape = 'line'
                elif event.key == pygame.K_t:
                    shape = 'triangle'
                elif event.key == pygame.K_h:
                    shape = 'rhombus'
                elif event.key == pygame.K_e:
                    mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                    drawing = True
                    start_pos = pygame.mouse.get_pos()
                elif event.button == 3:
                    radius = max(1, radius - 1)
                    drawing = False
                    if  start_pos is not None:
                        end_pos = pygame.mouse.get_pos()
                        radius = int(math.hypot(start_pos[0]-end_pos[0], start_pos[1]-end_pos[1]))
                        circles.append((start_pos, radius))  # Add the circle's position and radius to the list
                    start_pos = None

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))

        # Draw all circles
        for circle_pos, circle_radius in circles:
            pygame.draw.circle(screen, mode, circle_pos, circle_radius)

        i = 0
        while i < len(points) - 1:
            if shape == 'line':
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            elif shape == 'circle' and start_pos is not None:
                end_pos = pygame.mouse.get_pos()
                radius = int(math.hypot(start_pos[0]-end_pos[0], start_pos[1]-end_pos[1]))
                pygame.draw.circle(screen, mode, start_pos, radius)
            elif shape == 'square':
                pos = pygame.mouse.get_pos()
                startx = pos[0]
                starty = pos[1]
                pygame.draw.rect(screen, mode,(min(pos[0], startx), min(pos[1], starty), abs(pos[0] - startx), abs(pos[1] - starty)))
            elif shape == 'triangle':
                pygame.draw.polygon(screen, mode, [(points[i][0], points[i][1] - radius), (points[i][0] - radius, points[i][1] + radius), (points[i][0] + radius, points[i][1] + radius)], 0)
            elif shape == 'rhombus':
                pygame.draw.polygon(screen, mode, [(points[i][0], points[i][1] - radius), (points[i][0] - radius, points[i][1]), (points[i][0], points[i][1] + radius), (points[i][0] + radius, points[i][1])], 0)
            elif mode == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), points[i], radius)
            i += 1

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
