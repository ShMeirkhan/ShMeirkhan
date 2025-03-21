import pygame
import sys
import time
from math import sin, cos, radians
pygame.init()
width, height = 1400, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")
background = pygame.image.load('mickeyclock.png')
mickey = pygame.image.load('mickeyclock.png')
minute_hand = pygame.image.load('min_hand.png')
second_hand = pygame.image.load('sec_hand.png')
background_rect = background.get_rect(center=(width // 2, height // 2))
mickey_rect = mickey.get_rect(center=(width // 2, height // 2))
minute_hand_rect = minute_hand.get_rect(center=(width // 2, height // 2))
second_hand_rect = second_hand.get_rect(center=(width // 2, height // 2))

def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

  
    minute_angle = -6 * minutes  
    second_angle = -6 * seconds  

   
    screen.fill((255, 255, 255))
    screen.blit(background, background_rect)
    screen.blit(mickey, mickey_rect)
    blit_rotate_center(screen, minute_hand, minute_hand_rect.topleft, minute_angle)
    blit_rotate_center(screen, second_hand, second_hand_rect.topleft, second_angle)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()