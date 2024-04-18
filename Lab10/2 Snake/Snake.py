import pygame  # Import the pygame library
import random  # Import the random library

pygame.init()  # Initialize all imported pygame modules
clock = pygame.time.Clock()  # Create a new Clock object that can be used to track an amount of time
screen = pygame.display.set_mode((600, 600))  # Initialize a window or screen for display

done = False  # Boolean to keep the game running until user quits

# Define some colors
Red = (255, 0, 0)
Green = (0, 255, 0)
White = (255, 255, 255)
Black = (0, 0, 0)

# Define some variables for use in the program
speed = 5
score = 0
level = 1

# Set up fonts
font = pygame.font.Font(None, 28)

def save_score(username, score):
    with open('userdata.txt', 'r') as f:
        lines = f.readlines()
    with open('userdata.txt', 'w') as f:
        for line in lines:
            user, _ = line.split()
            if user == username:
                line = f'{username} {score}\n'
            f.write(line)

def get_level(username):
    with open('userdata.txt', 'r') as f:
        for line in f:
            user, score = line.split()
            if user == username:
                return int(score)
    return None

def add_user(username):
    with open('userdata.txt', 'a') as f:
        f.write(f'{username} 1\n')

username = input('Input your username: ')
level = get_level(username)
if level is not None:
    print(f'Welcome back {username}, you are currently on level: {level}')
else:
    add_user(username)
    level = 1
    print(f'Welcome {username}! You are starting on level 1.')

class Snake():
    def __init__(self):
        self.size = 1  # Initial size of the snake
        self.dx = 1  # Change in x-direction
        self.dy = 0  # Change in y-direction
        self.elements = [[100, 100]]  # Initial position of the snake

    def update(self, speed):  # Define the update method with 'speed' as a parameter
        # This method updates the position of the snake
        for i in range(self.size - 1, 0, -1):  # Loop backwards from the last element of the snake to the second element
            self.elements[i][0] = self.elements[i - 1][0]  # Set the x-coordinate of the current element to the x-coordinate of the previous element
            self.elements[i][1] = self.elements[i - 1][1]  # Set the y-coordinate of the current element to the y-coordinate of the previous element
            # The above loop shifts the positions of the snake's body segments to follow the segment in front of them
        self.elements[0][0] += self.dx * speed  # Update the x-coordinate of the snake's head based on its current direction (dx) and speed
        self.elements[0][1] += self.dy * speed  # Update the y-coordinate of the snake's head based on its current direction (dy) and speed

    def draw(self):
        # Draw the snake on the screen
        for element in self.elements:
            pygame.draw.circle(screen, Red, element, 10)

class Food():
    def __init__(self):
        self.x = random.randint(50, 550)  # Random x-coordinate for the food
        self.y = random.randint(150, 550)  # Random y-coordinate for the food
        self.weight = random.randint(1, 3)  # Random weight for the food
        self.creation_time = pygame.time.get_ticks()  # Record the creation time of the food

    def draw(self):
        # Draw the food on the screen
        pygame.draw.circle(screen, Green, (self.x, self.y), 10)

    def check_time(self):
        # If the food has existed for more than 3 seconds, it disappears
        if pygame.time.get_ticks() - self.creation_time > 3000:
            return True
        return False

# Create a Food object and a Snake object
food = Food()
snake = Snake()

# Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # End the game if the user quits

    # Check for key presses and update the direction of the snake accordingly
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and snake.dx:
        snake.dx = 0
        snake.dy = 1
        speed = -abs(speed)
    if pressed[pygame.K_DOWN] and snake.dx:
        snake.dx = 0
        snake.dy = 1
        speed = abs(speed)
    if pressed[pygame.K_LEFT] and snake.dy:
        snake.dx = 1
        snake.dy = 0
        speed = -abs(speed)
    if pressed[pygame.K_RIGHT] and snake.dy:
        snake.dx = 1
        snake.dy = 0
        speed = abs(speed)

    # Update the position of the snake
    snake.update(speed)

    # Draw the game elements on the screen
    screen.fill(White)
    text = font.render("Score: " + str(score), True, Black)
    screen.blit(text, (10, 10))
    text = font.render("Level: " + str(level), True, Black)
    screen.blit(text, (10, 30))
    snake.draw()
    food.draw()

    # Get the current position of the snake
    x = snake.elements[0][0]
    y = snake.elements[0][1]

    # End the game if the snake hits the boundary of the screen
    if x - 10 < 0 or x + 10 > 600 or y - 10 < 52 or y + 10 > 600:
        save_score(username, level)
        done = True

    # Check if the food should disappear
    if food.check_time():
        food = Food()  # Create a new food

    # Check if the snake has eaten the food
    if abs(x - food.x) + abs(y - food.y) < 20:
        score += food.weight  # Increase the score by the weight of the food
        if score % 3 == 0: # If the score is a multiple of 3
            level += 1     # Add level
            if speed > 0: speed += 1 # And increase speed
        snake.elements.append([0, 0])
        snake.size += 1
        food = Food()  # Create a new food

    pygame.display.flip()  # Update the full display Surface to the screen
    clock.tick(60)  # This method should be called once per frame
