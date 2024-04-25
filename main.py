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

    pos1, pos2, pos3 = (math.cos(i/180 * math.pi) * 250 + 300, math.sin(i/180 * math.pi) * 250 + 300), (math.cos(i * 1.1/180 * math.pi) * 250 + 300, math.sin(i * 1.1/180 * math.pi) * 250 + 300), (math.cos(i * 1.2/180 * math.pi) * 250 + 300, math.sin(i * 1.2/180 * math.pi) * 250 + 300)
    pygame.draw.circle(screen, (0, 0, 0), pos1, 10)
    pygame.draw.circle(screen, (0, 0, 0), pos2, 10)
    pygame.draw.circle(screen, (0, 0, 0), pos3, 10)
    pygame.draw.line(screen, (50, 50, 50), pos1, pos2, 3)
    pygame.draw.line(screen, (50, 50, 50), pos3, pos2, 3)
    pygame.draw.line(screen, (50, 50, 50), pos1, pos3, 3)
    i += 1

    pygame.display.update()
    fps_counter.tick(fps)
