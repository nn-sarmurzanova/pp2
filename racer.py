import pygame
import random


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


player_speed = 5
enemy_speed = 3
coin_speed = 5
N_COINS_TO_INCREASE_SPEED = 5


class Player(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
        self.speed = player_speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH), -50)
        self.speed = enemy_speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = -50

class Coin(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surface((20, 20))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 20)
        self.rect.y = random.randint(-100, -20)
        self.weight = random.randint(1, 3)  # Вес монеты

    def update(self):
        self.rect.y += coin_speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - 20)
            self.rect.y = random.randint(-100, -20)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")


player = Player()
enemy = Enemy()
coins = pygame.sprite.Group()
for _ in range(5):
    coin = Coin()
    coins.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coins)


score = 0
running = True


while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    all_sprites.update()

    
    if pygame.sprite.collide_rect(player, enemy):
        print("Game Over!")
        running = False

    
    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    for coin in collected_coins:
        score += coin.weight
        print(f"Score: {score}")

    
    if score >= N_COINS_TO_INCREASE_SPEED:
        enemy.speed = 6

    
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()