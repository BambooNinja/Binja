import pygame
import os
import sys
import math

pygame.init()

screen_size = (1920, 1080)

screen = pygame.display.set_mode(screen_size)
pygame.display.toggle_fullscreen()

fps_counter = pygame.time.Clock()
fps = 200

i = 0

# Fuck You

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))

    pygame.display.update()
    fps_counter.tick(fps)
