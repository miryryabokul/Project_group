import random
import pygame
import consts
import game_field


screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("The Flag Game")
flag_img = pygame.image.load("flag.png")
flag_img = pygame.transform.scale(flag_img, (4 * consts.PIXEL_PER_BLOCK_COL,3 * consts.PIXEL_PER_BLOCK_ROW))
grass_img = pygame.image.load("grass.png")
grass_img = pygame.transform.scale(grass_img,(4 * consts.PIXEL_PER_BLOCK_COL, 4 * consts.PIXEL_PER_BLOCK_ROW))
mine_img = pygame.image.load("mine.png")
mine_img = pygame.transform.scale(mine_img,(3 * consts.PIXEL_PER_BLOCK_COL, 1 * consts.PIXEL_PER_BLOCK_ROW))
soldier_img = pygame.image.load("soldier.png")
soldier_img = pygame.transform.scale(soldier_img,(2*consts.PIXEL_PER_BLOCK_COL,4*consts.PIXEL_PER_BLOCK_ROW))

def grass():
    grass_loaction=[]
    for i in range(20):
        list=draw_random()
        grass_loaction.append(list)
    return grass_loaction

def background_normal(grass_location):
    screen.fill(consts.DEFAULT_BACKGROUND_COLOR)
    for i in grass_location:
        screen.blit(grass_img,(i[0],i[1]))
    screen.blit(flag_img,(consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

def grid():
    screen.fill(consts.BLACK)
    for row in range(consts.MAT_ROW):
        pygame.draw.line(screen,consts.DEFAULT_BACKGROUND_COLOR,(0,row*consts.PIXEL_PER_BLOCK_ROW),(consts.SCREEN_WIDTH,row*consts.PIXEL_PER_BLOCK_ROW))
    for cal in range(consts.MAT_COL):
        pygame.draw.line(screen, consts.DEFAULT_BACKGROUND_COLOR,(0,cal * consts.PIXEL_PER_BLOCK_COL),(consts.SCREEN_HEIGHT, cal*consts.PIXEL_PER_BLOCK_COL))

def mine():
    mine_location=game_field.random_mines()
    for i in mine_location:
        screen.blit(mine_img, (i[0],i[1]))

def solider_draw():
    location=soldier.solider_loaction()
    screen.blit(soldier_img,(location[0],location[1]))

def draw_random():
    x=random.randrange(0,consts.SCREEN_WIDTH)
    y= random.randrange(0, consts.SCREEN_HEIGHT)
    list=(x,y)
    return list
print(hello )
