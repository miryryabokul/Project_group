import random
import pygame
import consts
import game_field

screen = pygame.display.set_mode(
        (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("The Flag Game")

flag_img = pygame.image.load("flag.png")
flag_img = pygame.transform.scale(flag_img,(4 * consts.PIXEL_PER_BLOCK_COL, 3 * consts.PIXEL_PER_BLOCK_ROW))
grass_img = pygame.image.load("grass.png")
grass_img = pygame.transform.scale(grass_img,(4 * consts.PIXEL_PER_BLOCK_COL, 4 * consts.PIXEL_PER_BLOCK_ROW))
mine_img = pygame.image.load("mine.png")
mine_img = pygame.transform.scale(mine_img,(3 * consts.PIXEL_PER_BLOCK_COL, 1 * consts.PIXEL_PER_BLOCK_ROW))
soldier_img = pygame.image.load("soldier.png")
soldier_img = pygame.transform.scale(soldier_img,(2*consts.PIXEL_PER_BLOCK_COL,4*consts.PIXEL_PER_BLOCK_ROW))

def grass():
    grass_location=[]
    for i in range(20):
        list=draw_random()
        grass_location.append(list)
    return grass_location

def background_normal(grass_location,list):
    screen.fill(consts.DEFAULT_BACKGROUND_COLOR)
    screen.blit(flag_img, (consts.SCREEN_WIDTH-4 * consts.PIXEL_PER_BLOCK_COL,consts.SCREEN_HEIGHT- 3 * consts.PIXEL_PER_BLOCK_ROW))
    for i in grass_location:
        screen.blit(grass_img,(i[0],i[1]))
    solider_draw(list)

def grid(mine_location,a,b):
    screen.fill(consts.BLACK)
    solider_draw(a,b)
    for row in range(consts.MAT_ROW):
        pygame.draw.line(screen,consts.DEFAULT_BACKGROUND_COLOR,(0,row*consts.PIXEL_PER_BLOCK_ROW),(consts.SCREEN_WIDTH,row*consts.PIXEL_PER_BLOCK_ROW))
    for cal in range(consts.MAT_COL):
        pygame.draw.line(screen,consts.DEFAULT_BACKGROUND_COLOR,(cal*consts.PIXEL_PER_BLOCK_COL,0),(cal*consts.PIXEL_PER_BLOCK_COL,consts.SCREEN_HEIGHT))
    mine(mine_location)

def mine(mine_location):
    for i in mine_location:
        screen.blit(mine_img, (i[0],i[1]))

def solider_draw(list):
    screen.blit(soldier_img,(list[0],list[1]))



