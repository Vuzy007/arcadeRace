import pygame
import random
import sys

# Инициализация
pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Racing Game")

# Загрузка картинок
player_img = pygame.image.load('player_car.png').convert_alpha()
enemy_img = pygame.image.load('enemy_car.png').convert_alpha()

# Машинка игрока
player_x = WIDTH // 2 - player_img.get_width() // 2
player_y = HEIGHT - player_img.get_height() - 20
player_speed = 5

# Встречные машины
enemies = []
enemy_speed = 5
spawn_timer = 0

# Игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # 60 FPS
    win.fill((30, 30, 30))  # Серый фон дороги

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_img.get_width():
        player_x += player_speed

    # Спавн встречных машин
    spawn_timer += 1
    if spawn_timer > 50:
        spawn_x = random.randint(0, WIDTH - enemy_img.get_width())
        enemies.append([spawn_x, -enemy_img.get_height()])
        spawn_timer = 0

    # Движение встречных машин
    for enemy in enemies:
        enemy[1] += enemy_speed
        win.blit(enemy_img, (enemy[0], enemy[1]))

    # Удаление вышедших за экран
    enemies = [e for e in enemies if e[1] < HEIGHT]

    # Проверка столкновений
    player_rect = pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_img.get_width(), enemy_img.get_height())
        if player_rect.colliderect(enemy_rect):
            print("CRASH!")
            running = False

    # Отрисовка игрока
    win.blit(player_img, (player_x, player_y))

    pygame.display.flip()
