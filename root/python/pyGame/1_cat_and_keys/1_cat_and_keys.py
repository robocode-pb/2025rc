import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Параметри екрана
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Завантаження зображень
cat_image = pygame.image.load('cat.png')
key_image = pygame.image.load('key.png')

# Масштабування зображень
cat_image = pygame.transform.scale(cat_image, (50, 50))
key_image = pygame.transform.scale(key_image, (30, 30))

# Початкові параметри героя
cat_x, cat_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
cat_speed = 5

# Початкові параметри ключа
key_x = random.randint(0, SCREEN_WIDTH - 30)
key_y = random.randint(0, SCREEN_HEIGHT - 30)

# Лічильник зібраних ключів
keys_collected = 0

# Шрифт для тексту
font = pygame.font.Font(None, 36)

# Головний цикл гри
running = True
while running:
    screen.fill(BLACK)
    
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Управління героєм
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cat_x -= cat_speed
    if keys[pygame.K_RIGHT]:
        cat_x += cat_speed
    if keys[pygame.K_UP]:
        cat_y -= cat_speed
    if keys[pygame.K_DOWN]:
        cat_y += cat_speed

    # Перевірка виходу за межі екрана
    cat_x = max(0, min(cat_x, SCREEN_WIDTH - 50))
    cat_y = max(0, min(cat_y, SCREEN_HEIGHT - 50))

    # Перевірка зіткнення героя з ключем
    cat_rect = pygame.Rect(cat_x, cat_y, 50, 50)
    key_rect = pygame.Rect(key_x, key_y, 30, 30)
    if cat_rect.colliderect(key_rect):
        keys_collected += 1
        key_x = random.randint(0, SCREEN_WIDTH - 30)
        key_y = random.randint(0, SCREEN_HEIGHT - 30)

    # Відображення тексту
    screen.blit(font.render(f"Зібрано ключів: {keys_collected}", True, WHITE), (10, 10))

    # Малювання героя та ключа
    screen.blit(cat_image, (cat_x, cat_y))
    screen.blit(key_image, (key_x, key_y))

    # Оновлення екрану
    pygame.display.flip()

    # Затримка
    pygame.time.Clock().tick(60)

pygame.quit()
