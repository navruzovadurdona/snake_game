import pygame
import random

# Инициализация
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Начальное состояние
clock = pygame.time.Clock()
speed = 10
snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
score = 0
font = pygame.font.SysFont('Arial', 24)

# Функции
def draw_snake(snake):
    for pos in snake:
        pygame.draw.rect(win, GREEN, (*pos, CELL_SIZE, CELL_SIZE))

def draw_food(pos):
    pygame.draw.rect(win, RED, (*pos, CELL_SIZE, CELL_SIZE))

def draw_score(score):
    text = font.render(f"Счёт: {score}", True, BLACK)
    win.blit(text, (10, 10))

# Игровой цикл
running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)

    # Движение змейки
    head = snake[-1]
    new_head = (head[0] + snake_dir[0], head[1] + snake_dir[1])
    snake.append(new_head)

    # Проверка еды
    if new_head == food:
        score += 1
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    else:
        snake.pop(0)

    # Столкновения
    if (
        new_head in snake[:-1] or
        not 0 <= new_head[0] < WIDTH or
        not 0 <= new_head[1] < HEIGHT
    ):
        print("Игра окончена! Счёт:", score)
        running = False

    # Отрисовка
    win.fill(WHITE)
    draw_snake(snake)
    draw_food(food)
    draw_score(score)
    pygame.display.update()

pygame.quit()
