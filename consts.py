import pygame

INITIAL_PLACE = (0, 0)
DEFAULT_BACKGROUND_COLOR = (1,90,32)
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

FONT_NAME = "Calibri"
OPENING_MESSAGE = "Welcome to the flag game' \nHave Fun!"
OPENING_FONT_SIZE = int(0.005 * SCREEN_WIDTH)
BLACK = (0, 0, 0)
OPENING_MESSAGE_COLOR = BLACK
OPENING_MESSAGE_LOCATION = (20, 0)

FLAG_LOCATION = (SCREEN_HEIGHT - 30)


GRASS = pygame.image.load('grass.png')
GRASS = pygame.transform.scale(GRASS, (40, 20))

SOLDIER = pygame.image.load('soldier.png')
SOLDIER = pygame.transform.scale(SOLDIER, (20, 40))

SNAKE = pygame.image.load('snake.png')
SNAKE = pygame.transform.scale(SNAKE, (40, 20))

INJURY = pygame.image.load('injury.png')
INJURY = pygame.transform.scale(INJURY, (20, 40))

MINE = pygame.image.load('mine.png')
MINE = pygame.transform.scale(MINE, (30, 10))

MINE_IMG = pygame.image.load('mine.png')
MINE_IMG = pygame.transform.scale(MINE_IMG, (30, 10))