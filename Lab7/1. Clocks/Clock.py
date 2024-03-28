import pygame
import datetime

# Initialize the pygame module
pygame.init()

# Set the size of the pygame window
screen = pygame.display.set_mode((500, 400))

# Variable to keep the main loop running
running = True

# Create a clock object that can be used to control the framerate
clock = pygame.time.Clock()

# Load the images for the clock and the hands
main_clock = pygame.image.load("mainclock.png")
minute_hand = pygame.image.load(("rightarm.png"))
second_hand = pygame.image.load(("leftarm.png"))

# Scale the images to the desired size
main_clock = pygame.transform.scale(main_clock, (500, 400))
minute_hand = pygame.transform.scale(minute_hand, (500, 450))
second_hand = pygame.transform.scale(second_hand, (50, 480))

# Main loop
while running:
    # Event handling
    for event in pygame.event.get():
        # If the close button of the window is pressed
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Get the current time
    current_time = datetime.datetime.now()

    # Calculate the angle for the minute and second hands
    minute_angle = current_time.minute * 6 * -1
    second_angle = current_time.second * 6 * -1

    # Rotate the images of the hands according to the current time
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)

    # Draw the clock and the hands on the screen
    screen.blit(main_clock, main_clock.get_rect(center=screen.get_rect().center))
    screen.blit(rotated_minute_hand, rotated_minute_hand.get_rect(center=screen.get_rect().center))
    screen.blit(rotated_second_hand, rotated_second_hand.get_rect(center=screen.get_rect().center))

    # Update the display
    pygame.display.flip()

    # Limit the framerate to 50 FPS
    clock.tick(50)

# Quit pygame
pygame.quit()
