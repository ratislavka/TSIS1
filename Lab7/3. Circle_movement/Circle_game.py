import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))

done = False
clock = pygame.time.Clock()

x = 25
y = 25

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y >= 20:
        y -= 20
    if pressed[pygame.K_DOWN] and y <= 375:
        y += 20
    if pressed[pygame.K_LEFT] and x >= 20:
        x -= 20
    if pressed[pygame.K_RIGHT] and x <= 375:
        x += 20

    color = (255, 0, 0)

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, (x, y), 25)

    pygame.display.flip()
    clock.tick(60)
