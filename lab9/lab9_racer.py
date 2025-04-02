import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

ROAD_IMAGE = pygame.image.load("road.png")
ROAD_IMAGE = pygame.transform.scale(ROAD_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("red.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        self.speed = 6

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png")
        self.image = pygame.transform.scale(self.image, (60, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coinn.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        self.weight = random.randint(1, 5)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        font = pygame.font.SysFont(None, 24)
        weight_text = font.render(str(self.weight), True, BLACK)
        weight_rect = weight_text.get_rect(center=self.rect.center)
        surface.blit(weight_text, weight_rect)

def restart_game():
    global score
    global player_group, enemy_group, coin_group
    global P1, E1, coin

    score = 0
    P1 = Player()
    E1 = Enemy()
    coin = Coin()

    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()

    player_group.add(P1)
    enemy_group.add(E1)
    coin_group.add(coin)

def game_over_screen():
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("Game Over", True, BLACK)
    restart_text = font.render("Press R to Restart or Q to Quit", True, BLACK)
    game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    restart_text_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    DISPLAYSURF.blit(game_over_text, game_over_text_rect)
    DISPLAYSURF.blit(restart_text, restart_text_rect)
    pygame.display.update()

P1 = Player()
E1 = Enemy()
coin = Coin()

player_group = pygame.sprite.Group(P1)
enemy_group = pygame.sprite.Group(E1)
coin_group = pygame.sprite.Group(coin)

score = 0
font = pygame.font.SysFont(None, 36)
SPEED_INCREASE_THRESHOLD = 5

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()
    coin.move()

    if pygame.sprite.collide_rect(P1, coin):
        score += coin.weight

        coin = Coin()
        coin_group.empty()
        coin_group.add(coin)

        if score % SPEED_INCREASE_THRESHOLD == 0:
            E1.speed += 1

    if pygame.sprite.collide_rect(P1, E1):
        for _ in range(60):
            DISPLAYSURF.fill(WHITE)
            P1.rect.move_ip(0, -10)
            P1.draw(DISPLAYSURF)
            E1.draw(DISPLAYSURF)
            coin.draw(DISPLAYSURF)
            pygame.display.update()
            FramePerSec.tick(FPS)

        game_over_screen()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[K_r]:
                restart_game()
                break
            if keys[K_q]:
                pygame.quit()
                sys.exit()

    DISPLAYSURF.blit(ROAD_IMAGE, (0, 0))

    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    coin.draw(DISPLAYSURF)

    score_text = font.render(f"Coins: {score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (SCREEN_WIDTH - 150, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)
