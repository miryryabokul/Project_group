import random
import pygame
import consts
screen = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
pygame.display.set_caption('Flag Game')

def normal_screen():
    screen.fill(consts.DEFAULT_BACKGROUND_COLOR)
    pygame.display.flip()
    for i in range(20):
        draw_random(consts.GRASS)

def draw_random(picture):
    x = random.randrange(consts.SCREEN_WIDTH + 1)
    y = random.randrange(consts.SCREEN_HEIGHT + 1)
    screen.blit(picture, (x, y))
    pygame.display.flip()

def draw_matrix_screen():
    for row in range(consts.MAT_ROW):
        for cell in range(consts.MAT_COL):
            rect = pygame.rect(row,cell)
            pygame.draw.rect(screen,WHITE, rect)


