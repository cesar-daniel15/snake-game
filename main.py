import pygame
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Snake Game")
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake parameters
square_size = 10
initial_velocity = 10


# Function to get random food position
def food_position():
    food_x = round(random.randrange(0, width - square_size) / square_size) * square_size
    food_y = round(random.randrange(0, height - square_size) / square_size) * square_size
    return food_x, food_y


# Function to draw food
def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, green, [food_x, food_y, size, size])


# Function to draw snake
def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], size, size])


# Function to run the game
def run_game():
    end_game = False
    x = width / 2
    y = height / 2
    speed_x = 0
    speed_y = 0
    snake_size = 1
    pixels = []
    food_x, food_y = food_position()
    score = 0
    game_velocity = initial_velocity

    while not end_game:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and speed_x == 0:
                    speed_x = -square_size
                    speed_y = 0
                elif event.key == pygame.K_RIGHT and speed_x == 0:
                    speed_x = square_size
                    speed_y = 0
                elif event.key == pygame.K_UP and speed_y == 0:
                    speed_x = 0
                    speed_y = -square_size
                elif event.key == pygame.K_DOWN and speed_y == 0:
                    speed_x = 0
                    speed_y = square_size

        x += speed_x
        y += speed_y

        if x < 0 or x >= width or y < 0 or y >= height:
            end_game = True

        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        draw_snake(square_size, pixels)
        draw_food(square_size, food_x, food_y)

        if x == food_x and y == food_y:
            food_x, food_y = food_position()
            snake_size += 1
            score += 1
            game_velocity = initial_velocity + (snake_size // 5)  # Increase speed

        font = pygame.font.SysFont(None, 35)
        text = font.render(f"Score: {score}", True, red)
        screen.blit(text, [0, 0])

        pygame.display.update()
        clock.tick(game_velocity)


run_game()
pygame.quit()
