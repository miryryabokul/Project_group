import pygame

INITIAL_PLACE = (0, 0)
DEFAULT_BACKGROUND_COLOR = (1, 90, 37)
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
MAT_ROW = 25
MAT_COL = 50
FONT_NAME = "Calibri"
OPENING_MESSAGE = "Welcome to the flag game' \nHave Fun!"
OPENING_FONT_SIZE = int(0.005 * SCREEN_WIDTH)
BLACK = (0, 0, 0)
OPENING_MESSAGE_COLOR = BLACK
OPENING_MESSAGE_LOCATION = (20, 0)

FLAG_LOCATION = (SCREEN_HEIGHT - 30, SCREEN_WIDTH - 40)
X_LOCATION = 0
Y_LOCATION = 0


GRASS = pygame.image.load('grass.png')
GRASS = pygame.transform.scale(GRASS, (45, 50))

SOLDIER = pygame.image.load('soldier.png')
SOLDIER = pygame.transform.scale(SOLDIER, (20, 40))

SNAKE = pygame.image.load('snake.png')
SNAKE = pygame.transform.scale(SNAKE, (40, 20))

INJURY = pygame.image.load('injury.png')
INJURY = pygame.transform.scale(INJURY, (20, 40))

MINE = pygame.image.load('mine.png')
MINE = pygame.transform.scale(MINE, (30, 10))

FLAG = pygame.image.load('flag.png')
FLAG = pygame.transform.scale(FLAG, (40, 30))

