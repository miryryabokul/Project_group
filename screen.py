import pygame
import consts
import game_field

screen = pygame.display.set_mode(
        (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("The Flag Game")

flag_img = pygame.image.load("flag.png")
flag_img = pygame.transform.scale(flag_img,
                                  (consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
grass_img = pygame.image.load("grass.png")
grass_img = pygame.transform.scale(grass_img,
                                   (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
mine_img = pygame.image.load("mine.png")
mine_img = pygame.transform.scale(mine_img,
                                  (consts.MINE_WIDTH, consts.MINE_HEIGHT))
soldier_img = pygame.image.load("soldier.png")
soldier_img = pygame.transform.scale(soldier_img, (consts.SOLDIER_WIDTH,
                                                   consts.SOLDIER_HEIGHT))


def background_normal(grass_location):
    screen.fill(consts.DEFAULT_BACKGROUND_COLOR)
    screen.blit(flag_img, (consts.SCREEN_WIDTH - 4 * consts.PIXEL_PER_BLOCK,
                           consts.SCREEN_HEIGHT - 3 * consts.PIXEL_PER_BLOCK))
    for i in grass_location:
        screen.blit(grass_img, (i[0], i[1]))


def grid(mine_location, soldier_location):
    screen.fill(consts.BLACK)
    solider_draw(soldier_location)
    for row in range(consts.MAT_ROW):
        pygame.draw.line(screen, consts.DEFAULT_BACKGROUND_COLOR,
                         (0, row * consts.PIXEL_PER_BLOCK),
                         (consts.SCREEN_WIDTH, row * consts.PIXEL_PER_BLOCK))
    for cal in range(consts.MAT_COL):
        pygame.draw.line(screen, consts.DEFAULT_BACKGROUND_COLOR,
                         (cal * consts.PIXEL_PER_BLOCK, 0),
                         (cal * consts.PIXEL_PER_BLOCK, consts.SCREEN_HEIGHT))
    mine(mine_location)


def mine(mine_location):
    for i in mine_location:
        screen.blit(mine_img, (i[0], i[1]))


def solider_draw(list):
    screen.blit(soldier_img, (list[0], list[1]))
