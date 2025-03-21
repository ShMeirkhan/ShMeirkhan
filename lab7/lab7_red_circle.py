import pygame
import sys

pygame.init()

screen_width, screen_height = 1100, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Move the Red Ball')

ball_color = (255, 0, 0)
ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2
ball_speed = 20

background_color = (255, 255, 255)

while True:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius < screen_height:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < screen_width:
        ball_x += ball_speed

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
