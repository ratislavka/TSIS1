# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
collected_coins = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.scale_factor = 0.1  # Adjust this value to get your desired size
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale_factor), int(self.image.get_height() * self.scale_factor)))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.value = random.randint(1, 3)  # Random cost for the coin

    def move(self):
        global collected_coins
        self.rect.move_ip(0, 3)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            self.weight = random.randint(1, 3)  # Randomly assign a new weight when the coin reappears

    def collect(self, player):
        global collected_coins
        if self.rect.colliderect(player.rect):
            collected_coins += self.weight  # Increase the number of collected coins by the weight of the coin
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Create multiple coins
coins = [Coin() for _ in range(5)]  # Change the range to the number of coins you want

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
# Add the coins to the sprite groups
all_sprites.add(*coins)

"""# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)"""

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
#        if event.type == INC_SPEED:
#           SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Create a new surface for the collected coins score
    collected_coins_display = font_small.render(str(collected_coins), True, BLACK)
    DISPLAYSURF.blit(collected_coins_display, (SCREEN_WIDTH - collected_coins_display.get_width() - 10, 10))


    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check for collisions between the player and each coin
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            collected_coins += coin.value  # Increase the score by the value of the coin
            coin.rect.top = 0
            coin.rect.center = (random.randint(30, 370), 0)
            coin.value = random.randint(1, 3)  # Assign a new random value to the coin

    # Increase game speed after every 10 points
    if collected_coins % 10 == 0 and collected_coins != 0:
        SPEED += 0.05

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)

