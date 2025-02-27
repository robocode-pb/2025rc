import pygame, random

# Константи
SCREEN_WIDTH    = 1500
SCREEN_HEIGHT   = 1000
CELL_SIZE       = 50
INITIAL_SPEED   = 10
APPLE_ADD_SPEED = 2
FONT_SIZE       = 36

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)


# Ініціалізація Pygame
pygame.init()

# Шрифт для тексту
font = pygame.font.Font(None, FONT_SIZE)

# Параметри екрана
screen = pygame.display.set_mode((
    SCREEN_WIDTH  // CELL_SIZE * CELL_SIZE,
    SCREEN_HEIGHT // CELL_SIZE * CELL_SIZE))
pygame.display.set_caption("Snake Game")

# Початкові параметри
def reset_game():
    """Скидає параметри гри до початкових."""
    global snake, direction, apples_collected, apple, tick_speed
    snake = [[  # Початкова позиція
        (SCREEN_WIDTH  // CELL_SIZE ) * CELL_SIZE / 2,
        (SCREEN_HEIGHT // CELL_SIZE ) * CELL_SIZE / 2,
    ]] 
    direction = [0, 0]   # Початковий напрям вправо
    apples_collected = 0 # З'їджені яблука
    apple = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
             random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
    tick_speed = INITIAL_SPEED # кількість кадів на секунду
reset_game()

def createRect(x, y): # 
    return pygame.Rect(x, y, CELL_SIZE-2, CELL_SIZE-2)

def printText(text, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))

def drawGrid():
    # Малюємо вертикальні лінії
    for x in range(-2, SCREEN_WIDTH + 1, CELL_SIZE):
        pygame.draw.line(screen, (20, 20, 20), (x, 0), (x, SCREEN_HEIGHT), 1)

    # Малюємо горизонтальні лінії
    for y in range(-2, SCREEN_HEIGHT + 1, CELL_SIZE):
        pygame.draw.line(screen, (20, 20, 20), (0, y), (SCREEN_WIDTH, y), 1)

# Основний цикл програми
while True:
    screen.fill(BLACK)
    drawGrid()
    
    # Обробка подій
    if pygame.event.peek(pygame.QUIT): pygame.quit()

    # Управління героєм
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and direction != (1,  0):
        direction = (-1, 0)
    if keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1,  0)
    if keys[pygame.K_UP]    and direction != (0,  1):
        direction = (0, -1)
    if keys[pygame.K_DOWN]  and direction != (0, -1):
        direction = (0,  1)

    # Рух змійки
    new_head = [snake[0][0] + direction[0] * CELL_SIZE, 
                snake[0][1] + direction[1] * CELL_SIZE]
    snake = [new_head] + snake[:-1]

    # Перевірка виходу за межі екрана
    if (snake[0][0] < 0 or snake[0][0] >= SCREEN_WIDTH  or 
        snake[0][1] < 0 or snake[0][1] >= SCREEN_HEIGHT or
        snake[0] in snake[1:] # Зіткнення з собою
    ):  
        printText("Гра закінчена! Перезапуск", RED, 
                  SCREEN_WIDTH // 2 - 200, 
                  SCREEN_HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(1000)
        reset_game()

    # Малювання змійки
    for segment in snake:
        pygame.draw.rect(screen, WHITE, createRect(segment[0], segment[1]))

    # Перевірка зіткнення з яблуком
    if createRect(*snake[0]).colliderect(createRect(*apple)):
        apples_collected += 1
        if apples_collected % APPLE_ADD_SPEED == 0 :tick_speed += 1
        while True: # Спавн яблука доти, доки воно на змійці
            new_apple = [
                random.randint(0, SCREEN_WIDTH  // CELL_SIZE - 1) * CELL_SIZE,
                random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE
            ]
            if new_apple not in snake:
                apple = new_apple
                break

        snake.append(snake[-1])  # Додати новий сегмент до кінця змійки

    # Малювання яблука
    pygame.draw.rect(screen, GREEN, createRect(apple[0], apple[1]))
    
    # Відображення тексту
    printText(f"Зібрано яблук: {apples_collected}", WHITE, 10, 10)
    printText(f"FPS: {tick_speed}", WHITE, SCREEN_WIDTH-110, 10)

    # Оновлення екрану
    pygame.display.flip()

    # Затримка
    pygame.time.Clock().tick(tick_speed)
