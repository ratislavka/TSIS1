import pygame
import math

pygame.init()
clock = pygame.time.Clock() # Create a new Clock object that can be used to track an amount of time
screen = pygame.display.set_mode((600, 800))  # Initialize a window or screen for display


done = False

colors = {
    "Red": (255, 0, 0),
    "White": (255, 255, 255),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Black": (0, 0, 0),

}

def intersect_rect(point, rect):   # Function to check if a point intersects with a rectangle
    if rect[0] <= point[0] <= rect[0] + rect[2] and rect[1] <= point[1] <= rect[1] + rect[3]: return True
    else: return False
def intersect_circle(point, start, radius):  # Function to check if a point intersects with a circle
    if math.sqrt((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2) <= radius: return True
    else: return False




radius = 10
mode = "Paint"
color = "Red"
points = []
rectangles = []
circles = []
squares = []
rhombuses = []
equilateral_triangles = []
right_triangles = []



startx = -1 # Initial x-coordinate for drawing shapes
starty = -1 # Initial y-coordinate for drawing shapes

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        done = True
    if pressed[pygame.K_1]:  # If the 1 key is pressed
        color = "Red"  # Change the color to red
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
    if pressed[pygame.K_w]:  # If the w key is pressed
        mode = "Rectangle"  # Change the mode to rectangle
        startx = -1  # Reset the starting x-coordinate
        starty = -1  # Reset the starting y-coordinate
    if pressed[pygame.K_e]:
        mode = "Circle"
        startx = -1
        starty = -1
    if pressed[pygame.K_h]:
        mode = "Rhombus"
        startx = -1
        starty = -1
    if pressed[pygame.K_s]:
        mode = "Square"
        startx = -1
        starty = -1
    if pressed[pygame.K_t]:
        mode = "EquilateralTriangle"
        startx = -1
        starty = -1
    if pressed[pygame.K_y]:
        mode = "RightTriangle"
        startx = -1
        starty = -1

    m_pressed = pygame.mouse.get_pressed() # Get the state of all mouse buttons
    if m_pressed[0] and mode == "Paint":  # If the left mouse button is pressed and the mode is paint
        radius += 1
        if radius > 50: radius = 50
    if m_pressed[2] and mode == "Paint":
        radius -= 1
        if radius < 1: radius = 1

    if m_pressed[0] and mode == "Rectangle": # If the left mouse button is pressed and the mode is rectangle
        if startx == -1:  # If the starting x-coordinate is not set
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

    if m_pressed[0] and mode == "Rhombus":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            radius = int(math.sqrt((pos[0] - startx) ** 2 + (pos[1] - starty) ** 2))
            rhombuses.append([[(startx, starty - radius), (startx - radius, starty), (startx, starty + radius),
                               (startx + radius, starty)], colors[color]])
            startx = -1
            starty = -1


    if m_pressed[0] and mode == "Square":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            side = max(abs(pos[0] - startx), abs(pos[1] - starty))
            squares.append(((min(pos[0], startx), min(pos[1], starty), side, side), colors[color]))
            startx = -1
            starty = -1
        if m_pressed[0] and mode == "EquilateralTriangle":
            if startx == -1:
                pos = pygame.mouse.get_pos()
                startx = pos[0]
                starty = pos[1]
            else:
                pos = pygame.mouse.get_pos()
                side = int(math.sqrt((pos[0] - startx) ** 2 + (pos[1] - starty) ** 2))
                equilateral_triangles.append([[(startx, starty),
                                               (startx + side // 2, starty - int(math.sqrt(3) * side // 2)),
                                               (startx + side, starty)], colors[color]])
                startx = -1
                starty = -1

        if m_pressed[0] and mode == "RightTriangle":
            if startx == -1:
                pos = pygame.mouse.get_pos()
                startx = pos[0]
                starty = pos[1]
            else:
                pos = pygame.mouse.get_pos()
                right_triangles.append([[(startx, starty), (pos[0], starty), (startx, pos[1])], colors[color]])
                startx = -1
                starty = -1

    if m_pressed[0] and mode == "EquilateralTriangle":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            side = int(math.sqrt((pos[0] - startx) ** 2 + (pos[1] - starty) ** 2))
            equilateral_triangles.append([[(startx, starty),
                                           (startx + side // 2, starty - int(math.sqrt(3) * side // 2)),
                                           (startx + side, starty)], colors[color]])
            startx = -1
            starty = -1

    if m_pressed[0] and mode == "RightTriangle":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            right_triangles.append([[(startx, starty), (pos[0], starty), (startx, pos[1])], colors[color]])
            startx = -1
            starty = -1

    if m_pressed[0] and mode == "Eraser":
        pos = pygame.mouse.get_pos()
        i = 0
        while i < len(rectangles):  # Loop through each rectangle in the list of rectangles
            if intersect_rect(pos,
                              rectangles[i][0]):  # If the current mouse position intersects with the current rectangle
                rectangles.pop(i)  # Remove the current rectangle from the list
            else:
                i += 1  # If the current mouse position does not intersect with the current rectangle, move to the next rectangle
        i = 0  # Reset the index to 0 for the next loop or operation

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


    for rect in rectangles:  # Loop through each rectangle in the list of rectangles
        pygame.draw.rect(screen, rect[1], rect[0])  # Draw each rectangle on the screen. rect[1] is the color and rect[0] is the rectangle's dimensions

    for circle in circles:  # Loop through each circle in the list of circles
        pygame.draw.circle(screen, circle[1], circle[0], circle[2])  # Draw each circle on the screen. circle[1] is the color, circle[0] is the center of the circle, and circle[2] is the radius

    for rhombus in rhombuses:  # Loop through each rhombus in the list of rhombuses
        pygame.draw.polygon(screen, rhombus[1], rhombus[0])  # Draw each rhombus on the screen. rhombus[1] is the color and rhombus[0] is the list of vertices

    for square in squares:  # Loop through each square in the list of squares
        pygame.draw.rect(screen, square[1], square[0])  # Draw each square on the screen. square[1] is the color and square[0] is the square's dimensions

    for triangle in equilateral_triangles:  # Loop through each equilateral triangle in the list of equilateral triangles
        pygame.draw.polygon(screen, triangle[1], triangle[0])  # Draw each equilateral triangle on the screen. triangle[1] is the color and triangle[0] is the list of vertices

    for triangle in right_triangles:  # Loop through each right triangle in the list of right triangles
        pygame.draw.polygon(screen, triangle[1], triangle[0])  # Draw each right triangle on the screen. triangle[1] is the color and triangle[0] is the list of vertices


    if mode == "Rectangle":  # If the current mode is "Rectangle"
        if startx != -1:  # If the starting x-coordinate is set (i.e., not -1)
            pos = pygame.mouse.get_pos()  # Get the current position of the mouse
            # Draw a rectangle on the screen. The color of the rectangle is determined by colors[color].
            # The position and dimensions of the rectangle are determined by the starting position (startx, starty) and the current mouse position.
            # The min function is used to ensure that the rectangle can be drawn in any direction.
            # The abs function is used to ensure that the width and height of the rectangle are always positive.
            pygame.draw.rect(screen, colors[color], (min(pos[0], startx), min(pos[1], starty), abs(pos[0] - startx), abs(pos[1] - starty)))


    if mode == "Circle":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, colors[color], (startx, starty), math.sqrt((pos[0] - startx) ** 2 + (pos[1] - starty) ** 2))

    if mode == "Rhombus":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            radius = int(math.sqrt((pos[0] - startx) ** 2 + (pos[1] - starty) ** 2))
            pygame.draw.polygon(screen, colors[color],
                                [[startx, starty - radius], [startx - radius, starty], [startx, starty + radius],
                                 [startx + radius, starty]], 0)
    if mode == "Square":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            side = max(abs(pos[0] - startx), abs(pos[1] - starty))
            pygame.draw.rect(screen, colors[color], (min(pos[0], startx), min(pos[1], starty), side, side))

    if mode == "EquilateralTriangle":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            side = int(math.sqrt((pos[0] - startx) ** 2 + (pos[1] - starty) ** 2))
            pygame.draw.polygon(screen, colors[color],
                                [[startx, starty], [startx + side // 2, starty - int(math.sqrt(3) * side // 2)],
                                 [startx + side, starty]])

    if mode == "RightTriangle":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            pygame.draw.polygon(screen, colors[color], [[startx, starty], [pos[0], starty], [startx, pos[1]]])

    pygame.display.flip()
    if mode == "Paint": clock.tick(200)
    else: clock.tick(60)


