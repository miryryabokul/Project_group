import random

import pygame
import consts
screen = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))
pygame.display.set_caption('Flag Game')

def normal_screen():
    screen.fill(consts.DEFAULT_BACKGROUND_COLOR)

def random_bush():
    bush_x = random.randint(consts.SCREEN_WIDTH+1)
    bush_y = random.randint(consts.SCREEN_HEIGHT+1)
    screen.bilt(grass,(bush_x,bush_y))

