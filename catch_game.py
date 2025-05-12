# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# WIDTH, HEIGHT = 600, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Catch the Falling Object")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)

# # Clock
# clock = pygame.time.Clock()
# FPS = 60

# # Basket (player)
# basket_width = 100
# basket_height = 20
# basket_x = WIDTH // 2 - basket_width // 2
# basket_y = HEIGHT - basket_height - 10
# basket_speed = 7

# # Falling object
# object_radius = 15
# object_x = random.randint(0, WIDTH - object_radius)
# object_y = 0
# object_speed = 5

# # Score
# score = 0
# font = pygame.font.SysFont(None, 36)

# # Game loop
# running = True
# while running:
#     screen.fill(WHITE)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Basket movement
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and basket_x > 0:
#         basket_x -= basket_speed
#     if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
#         basket_x += basket_speed

#     # Move falling object
#     object_y += object_speed

#     # Collision detection
#     if (basket_y < object_y + object_radius < basket_y + basket_height) and \
#        (basket_x < object_x < basket_x + basket_width):
#         score += 1
#         object_y = 0
#         object_x = random.randint(0, WIDTH - object_radius)

#     # Missed object
#     if object_y > HEIGHT:
#         object_y = 0
#         object_x = random.randint(0, WIDTH - object_radius)
#         score -= 1  # Or lose a life

#     # Draw basket and object
#     pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height))
#     pygame.draw.circle(screen, RED, (object_x, object_y), object_radius)

#     # Draw score
#     score_text = font.render(f"Score: {score}", True, BLACK)
#     screen.blit(score_text, (10, 10))

#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Basket (player)
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 7

# Falling object
object_radius = 15
object_x = random.randint(0, WIDTH - object_radius)
object_y = 0
object_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move falling object
    object_y += object_speed

    # Collision detection
    if (basket_y < object_y + object_radius < basket_y + basket_height) and \
       (basket_x < object_x < basket_x + basket_width):
        score += 1
        object_y = 0
        object_x = random.randint(0, WIDTH - object_radius)

    # Missed object
    if object_y > HEIGHT:
        object_y = 0
        object_x = random.randint(0, WIDTH - object_radius)
        score -= 1  # Or lose a life

    # Draw basket and object
    pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.circle(screen, RED, (object_x, object_y), object_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
