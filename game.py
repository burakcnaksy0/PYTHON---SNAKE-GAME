import pygame
import sys
import random

# Pygame başlat
pygame.init()

# Ekran boyutları
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yılan Oyunu")

# Renkler
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Yılanın başlangıç pozisyonu ve boyutu
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = (1, 0)  # Başlangıçta sağa hareket eder

# Yem başlangıç pozisyonu
food = (random.randint(0, (width-10)//10) * 10, random.randint(0, (height-10)//10) * 10)

# Oyun hızı ve zamanlayıcı
clock = pygame.time.Clock()
snake_speed = 15

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Klavye hareket kontrolü
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Yılanın hareketi
    new_head = (snake[0][0] + snake_direction[0] * 10, snake[0][1] + snake_direction[1] * 10)
    snake.insert(0, new_head)

    # Yılanın kendisine çarpmasını kontrol et
    if new_head in snake[1:]:
        pygame.quit()
        sys.exit()

    # Yılanın ekran sınırlarını kontrol et
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        pygame.quit()
        sys.exit()

    # Yılanın yem yemesini kontrol et
    if new_head == food:
        food = (random.randint(0, (width-10)//10) * 10, random.randint(0, (height-10)//10) * 10)
    else:
        snake.pop()

    # Ekranı temizle
    screen.fill(black)

    # Yılanı çiz
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], 10, 10))

    # Yemi çiz
    pygame.draw.rect(screen, red, (food[0], food[1], 10, 10))

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarla
    clock.tick(snake_speed)
