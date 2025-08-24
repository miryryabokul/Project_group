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

    draw_matrix_screen()
    pygame.display.flip()


def draw_random(picture):
    x = random.randrange(consts.SCREEN_WIDTH + 1)
    y = random.randrange(consts.SCREEN_HEIGHT + 1)
    screen.blit(picture, (x, y))
    pygame.display.flip()

def draw_matrix_screen():
    ((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))

    for row in range(0,1200,24):
        for cell in range(0,800,32):
            rect=pygame.Rect(row, cell,24,32)
            pygame.draw.rect(screen,consts.DEFAULT_BACKGROUND_COLOR,rect,1)


