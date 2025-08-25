import consts
import pygame
import sys


def create_field (game_field):
    for row in range (0, consts.MAT_ROW -1 ):
        x = []
        for col in range (0, consts.MAT_COL - 1):
            dict_cal={}
            dict_cal["x_location"]=row*30
            dict_cal["y_location"]=col*30
            dict_cal["role"]="EMPTY"
            x.append(dict_cal)
        game_field.append(x)
    return game_field


def check_win (soldier, flag):
    for i in range (soldier):
        if soldier[-1].colliderect(flag):
    #      print lose message for 3 sec
            pygame.quit()
            sys.exit()

