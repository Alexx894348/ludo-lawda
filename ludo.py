import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo Game")

# Dice roll function
def roll_dice():
    return random.randint(1, 6)

# Main game loop
running = True
dice_roll = 1
while running:
    screen.fill(WHITE)
    
    # Draw a simple board (just a placeholder for now)
    pygame.draw.rect(screen, RED, (50, 50, 200, 200))
    pygame.draw.rect(screen, GREEN, (350, 50, 200, 200))
    pygame.draw.rect(screen, YELLOW, (50, 350, 200, 200))
    pygame.draw.rect(screen, BLUE, (350, 350, 200, 200))
    
    # Display the dice roll
    font = pygame.font.Font(None, 36)
    text = font.render(f"Dice: {dice_roll}", True, BLACK)
    screen.blit(text, (250, 250))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_roll = roll_dice()
    
    pygame.display.flip()

pygame.quit()
