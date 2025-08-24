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


GRASS_IMG = pygame.image.load('grass.png')
GRASS_IMG = pygame.transform.scale(GRASS_IMG, (40, 20))

SOLDIER_IMG = pygame.image.load('soldier.png')
SOLDIER_IMG = pygame.transform.scale(SOLDIER_IMG, (20, 40))

SNAKE_IMG = pygame.image.load('snake.png')
SNAKE_IMG = pygame.transform.scale(SNAKE_IMG, (40, 20))

INJURY_IMG = pygame.image.load('injury.png')
INJURY_IMG = pygame.transform.scale(INJURY_IMG, (20, 40))

MINE_IMG = pygame.image.load('mine.png')
MINE_IMG = pygame.transform.scale(MINE_IMG, (30, 10))
