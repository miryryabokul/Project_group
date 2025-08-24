import random

import pygame
import consts
screen = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
pygame.display.set_caption('Flag Game')

def normal_screen():
    screen.fill(consts.DEFAULT_BACKGROUND_COLOR)
    for i in range(20):
        draw_random(grass)

def draw_random(picture):
    x = random.randint(consts.SCREEN_WIDTH + 1)
    y = random.randint(consts.SCREEN_HEIGHT + 1)
    screen.bilt(picture, (x, y))

def matrix_screen():
    pygame.draw.rect(screen,color,(x,y))
    for row in matrix:
        for item in row:
            pygame.draw.rect(screen, color, (row,item), 1)
    for j in range(20):
        draw_random(explotion)

