import pygame
import game_field
import screen
import consts
import sys

import soldier


def main():
    game = True
    clock = pygame.time.Clock()
    pygame.init()
    grass_location, mine_location = game_field.random_location()
    screen.background_normal(grass_location)
    soldier_location = [0, 0]
    screen.solider_draw(soldier_location)

    pygame.display.flip()
    while game:
        game, soldier_location = handle_user_event(game, soldier_location,
                                                   grass_location,
                                                   mine_location)

def handle_user_event(game, soldier_location, grass, mine):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.grid(mine, soldier_location)
                pygame.display.update()
                pygame.time.wait(1000)
                screen.background_normal(grass)
                screen.solider_draw(soldier_location)
                pygame.display.update()

            elif event.key == pygame.K_RIGHT:
                if soldier_location[
                    0] != consts.SCREEN_WIDTH - consts.PIXEL_PER_BLOCK:
                    screen.background_normal(grass)
                    soldier_location[0] += consts.PIXEL_PER_BLOCK
                    screen.solider_draw(soldier_location)
                    pygame.display.flip()

            elif event.key == pygame.K_LEFT:
                if soldier_location[0] != 0:
                    screen.background_normal(grass)
                    soldier_location[0] -= consts.PIXEL_PER_BLOCK
                    screen.solider_draw(soldier_location)
                    pygame.display.flip()

            elif event.key == pygame.K_DOWN:
                if soldier_location[
                    1] != consts.SCREEN_HEIGHT + consts.PIXEL_PER_BLOCK:
                    screen.background_normal(grass)
                    soldier_location[1] += consts.PIXEL_PER_BLOCK
                    screen.solider_draw(soldier_location)
                    pygame.display.flip()

            elif event.key == pygame.K_UP:
                if soldier_location[1] != 0:
                    screen.background_normal(grass)
                    soldier_location[1] -= consts.PIXEL_PER_BLOCK
                    screen.solider_draw(soldier_location)
                    pygame.display.flip()

    return game, soldier_location


if __name__ == "__main__":
    main()
