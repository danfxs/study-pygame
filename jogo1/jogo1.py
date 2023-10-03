import pygame
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((600, 400), 0, 32)

GAME_OVER = False

player_rect = pygame.Rect(30, 30, 60, 60)
BLUE = (0, 0, 255)

while not GAME_OVER:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= 5
            if event.key == pygame.K_RIGHT:
                player_rect.x += 5
    SCREEN.fill((0,0,0))
    rect_player = pygame.draw.rect(SCREEN, BLUE, player_rect)
    pygame.display.update()

pygame.quit()