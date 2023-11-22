import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 10
SNAKE_SPEED = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize Snake and Food
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = "RIGHT"
food_position = (random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE,
                 random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE)

# Score
score = 0

# Game Over Function
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Your Score: {score}", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = "UP"
            if event.key == pygame.K_DOWN:
                snake_direction = "DOWN"
            if event.key == pygame.K_LEFT:
                snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                snake_direction = "RIGHT"

    # Move the Snake
    if snake_direction == "UP":
        new_head = (snake[0][0], snake[0][1] - SNAKE_SIZE)
    if snake_direction == "DOWN":
        new_head = (snake[0][0], snake[0][1] + SNAKE_SIZE)
    if snake_direction == "LEFT":
        new_head = (snake[0][0] - SNAKE_SIZE, snake[0][1])
    if snake_direction == "RIGHT":
        new_head = (snake[0][0] + SNAKE_SIZE, snake[0][1])

    snake.insert(0, new_head)

    # Check for collision with food
    if snake[0] == food_position:
        score += 1
        food_position = (random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE,
                         random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE)
    else:
        snake.pop()

    # Check for collision with boundaries or itself
    if (snake[0][0] >= WIDTH or snake[0][0] < 0 or
        snake[0][1] >= HEIGHT or snake[0][1] < 0 or
        snake[0] in snake[1:]):
        game_over()

    # Fill the background
    screen.fill(BLACK)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw the food
    pygame.draw.rect(screen, RED, (food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Update the display
    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(SNAKE_SPEED)

