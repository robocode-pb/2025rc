# https://download-directory.github.io/?url=https://github.com/robocode-pb/2024rc/tree/main/Fr/WebMiddle/python/pyGame/1_v2_cat_and_keys

import pygame
import json
import random
import math

# Ініціалізація Pygame
pygame.init()

# Параметри екрану
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Integrated Game")

WHITE, BLACK = (255, 255, 255), (0, 0, 0)
FPS = 60
BULLET_SPEED = 5


class MapLoader:
    def __init__(self, scale=1):
        self.scale = scale
        self.background = pygame.image.load('TileMap/map.png').convert()
        self.background = pygame.transform.scale(self.background, 
                                                (SCREEN_WIDTH * self.scale, SCREEN_HEIGHT * self.scale))

    def draw(self):
        screen.blit(self.background, (0, 0))

# Базовий клас для об'єктів
class GameObject:
    def __init__(self, x=0, y=0, img_src=None, width=50, height=50, angle=0):
        self.x = x - width//2
        self.y = y - height //2
        if img_src:
            self.load_img(img_src, width, height, angle=angle)

    def load_img(self, src_img, width=50, height=50, angle=0):
        try:
            self.img = pygame.image.load(src_img)
            if angle:
                self.img = pygame.transform.rotozoom(self.img, angle, 1.0)
            self.img = pygame.transform.scale(self.img, (width, height))
            self.width, self.height = width, height
        except pygame.error as e:
            self.img = pygame.Surface((width, height))
            self.img.fill(WHITE)

    def random_position(self):
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = random.randint(0, SCREEN_HEIGHT - self.height)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    
    def __str__(self):
        result = []
        for key in dir(self):
            if not key.startswith("__"): 
                attr = getattr(self, key)
                if not callable(attr):
                    result.append(f"{key}: {repr(attr)}")
        return "   ".join(result)

class Entity(GameObject):
    def __init__(self, name, hp, attack, speed, x=0, y=0, img_src=None, width=50, height=50):
        super().__init__(x, y, img_src=img_src, width=width, height=height)
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed

class Player(Entity):
    def __init__(self, name, x, y, speed=5, img_src=None, width=50, height=50):
        super().__init__(name, speed=speed, hp=10, attack=2, x=x, y=y, img_src=img_src, width=width, height=height)
        self.level = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP]or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]or keys[pygame.K_s]:
            self.y += self.speed
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.height))

class Enemy(Entity):
    def move_towards(self, target):
        if self.x < target.x:
            self.x += self.speed
        elif self.x > target.x:
            self.x -= self.speed
        if self.y < target.y:
            self.y += self.speed
        elif self.y > target.y:
            self.y -= self.speed
    
    def random_position(self):
        self.x = random.randint(0, 1) * SCREEN_WIDTH
        self.y = random.randint(0, 1) * SCREEN_HEIGHT

class Bullet(GameObject):
    def __init__(self, x, y, speed=5, direction_x=0, direction_y=0, img_src=None, width=50, height=50, angle=0):
        super().__init__(x, y, img_src=img_src, width=width, height=height, angle=angle)
        self.speed = speed
        self.direction_x = direction_x
        self.direction_y = direction_y

    def move(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

bullets = []
def create_bullet(dx, dy):
    distance = math.sqrt(dx**2 + dy**2)
    if distance != 0:
        dx /= distance
        dy /= distance
    angle = math.degrees(math.atan2(-dy, dx))
    bullets.append(Bullet(player.x + player.width // 2, player.y, 
                          8, dx, dy, img_src="Sprite/bullet.png", angle=angle))


map = MapLoader(scale=1)

player = Player("Cat", 100, 100, speed=5,
                img_src="Sprite/cat.png", width=50, height= 50)

zombie = Enemy("Zombie", hp=10, speed=1, attack=1, x=400, y=300,
               img_src="Sprite/zombie.png",width= 30,height= 50)
zombie.random_position()

key = GameObject(img_src='Sprite/key.png')
key.random_position()

shop = GameObject(x=50, y=SCREEN_HEIGHT-50, img_src="Sprite/shop.png",width= 100,height= 150)

draw_objects = [map, player, zombie, key, shop]

font = pygame.font.Font(None, 36)
def print_text(text, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))

keys_collected = 0
running = True
clock = pygame.time.Clock()
pause = False
shop_open = False
# Головний цикл
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if shop.rect().collidepoint(mouse_x, mouse_y):
                shop_open = True
                pause = True  # Зупиняємо гру під час відкритого магазину
            if not pause:
                create_bullet(mouse_x - player.x, mouse_y - player.y)


    if shop_open:
        print_text("Welcome to the Shop! Press ESC to Exit Shop", WHITE, 50, 50)

        # Якщо натиснули ESC, закриваємо магазин
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            shop_open = False
            pause = False

    else:
        player.move()
        if not pause:
            zombie.move_towards(player)

        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect().colliderect(zombie.rect()):
                bullets.remove(bullet)
                zombie.hp -= player.attack
                if zombie.hp <= 0:
                    zombie.hp = 10
                    player.level += 1
                    zombie.random_position()
            elif not (0 <= bullet.x <= SCREEN_WIDTH and 0 <= bullet.y <= SCREEN_HEIGHT):
                bullets.remove(bullet)

        for object in draw_objects[:] + bullets[:]:
            object.draw()

        if pygame.Rect.colliderect(player.rect(), key.rect()):
            keys_collected += 1
            key.random_position()

        if pygame.Rect.colliderect(player.rect(), shop.rect()):
            if keys_collected >= 5:
                keys_collected -= 5
                player.level += 1


    print_text(f"Зібрано ключів: {keys_collected}", WHITE, 10, 10)
    print_text(f"LVL {player.level}", WHITE, 300, 10)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
