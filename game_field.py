import consts
import pygame
import sys
import random


def create_field(game_field):
    for row in range(0, consts.MAT_ROW - 1):
        x = []
        for col in range(0, consts.MAT_COL - 1):
            dict_cal = {}
            dict_cal["x_location"] = row * 30
            dict_cal["y_location"] = col * 30
            dict_cal["role"] = "EMPTY"
            x.append(dict_cal)
        game_field.append(x)
    return game_field


def random_location():
    grass_location = []
    mine_location = []
    for i in range(20):
        list = []
        x = random.randrange(consts.PIXEL_PER_BLOCK,
                             consts.SCREEN_WIDTH - consts.GRASS_WIDTH,
                             consts.PIXEL_PER_BLOCK)
        list.append(x)
        y = random.randrange(consts.PIXEL_PER_BLOCK,
                             consts.SCREEN_HEIGHT - consts.GRASS_HEIGHT,
                             consts.PIXEL_PER_BLOCK)
        list.append(y)
        grass_location.append(list)
    for j in range(20):
        list = []
        x = random.randrange(consts.PIXEL_PER_BLOCK,
                             consts.SCREEN_WIDTH - consts.MINE_WIDTH,
                             consts.PIXEL_PER_BLOCK)
        list.append(x)
        y = random.randrange(consts.PIXEL_PER_BLOCK,
                             consts.SCREEN_HEIGHT - consts.MINE_HEIGHT,
                             consts.PIXEL_PER_BLOCK)
        list.append(y)
        mine_location.append(list)
    return grass_location, mine_location


def check_win(soldier, flag):
    for i in range(soldier):
        if soldier[-1].colliderect(flag):
            #      print lose message for 3 sec
            pygame.quit()
            sys.exit()
