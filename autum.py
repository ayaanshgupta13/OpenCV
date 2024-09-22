import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Autumn Forest")
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Autumn Leaf Catcher")

# Load images
leaf_image = pygame.image.load("leaf.png")
basket_image = pygame.image.load("wicker-basket.png")
background_image = pygame.image.load("a.jpg")

# Scale images
leaf_image = pygame.transform.scale(leaf_image, (40, 40))
basket_image = pygame.transform.scale(basket_image, (100, 50))

# Game variables
basket_x = SCREEN_WIDTH // 2 - 50
basket_y = SCREEN_HEIGHT - 60
basket_speed = 10

leaf_x = random.randint(0, SCREEN_WIDTH - 40)
leaf_y = -40
leaf_speed = 5

score = 0
font = pygame.font.Font(None, 36)
z = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.blit(background_image, (0, 0))  # Draw background
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - 100:
        basket_x += basket_speed

    # Leaf movement
    leaf_y += leaf_speed
    if leaf_y > SCREEN_HEIGHT:
        leaf_x = random.randint(0, SCREEN_WIDTH - 40)
        leaf_y = -40
        z =+1 
        if z == 10:
            leaf_image = pygame.image.load('tropical-leaves.png')
            if basket_x < leaf_x < basket_x + 100 and basket_y < leaf_y + 40 < basket_y + 50:
                score =0
                leaf_x = random.randint(0, SCREEN_WIDTH - 40)
                leaf_y = -40
            z = 0
        else:
            leaf_image = pygame.image.load('leaf.png')
    # Check for collision
    if basket_x < leaf_x < basket_x + 100 and basket_y < leaf_y + 40 < basket_y + 50:
        score += 1
        leaf_x = random.randint(0, SCREEN_WIDTH - 40)
        leaf_y = -40

    # Draw basket
    screen.blit(basket_image, (basket_x, basket_y))

    # Draw leaf
    screen.blit(leaf_image, (leaf_x, leaf_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, YELLOW)
    screen.blit(score_text, (10, 10))

    if  score == 20:
        basket_x = 10000000000000000000000000000000000000
        basket_y = 10000000000000000000000000000000000000
        leaf_x = 1000000000000000000000000000000000000000
        leaf_y = 1000000000000000000000000000000000000000
        background_image = pygame.image.load('q.jpg')
        screen.blit(background_image,(0,0))
        time.sleep(3)

    # Update screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
pygame.quit()