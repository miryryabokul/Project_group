import pygame
import screen
import consts
import sys

def main():
    game=True
    clock = pygame.time.Clock()
    pygame.init()
    grass=screen.grass()
    screen.background_normal(grass,[0,0])
    soldier_location=[0,0]
    pygame.display.flip()
    while game:
        game,soldier_location=handle_user_event(game,soldier_location)

def handle_user_event(game,soldier_location,grass):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                screen.grid(soldier_location)
                pygame.time.wait(1000)
                screen.background_normal(grass,soldier_location)

            elif event.key == pygame.K_RIGHT:
               if soldier_location[0]!=consts.SCREEN_WIDTH:
                   soldier_location[0]+=consts.PIXEL_PER_BLOCK_COL
                   screen.solider_draw(soldier_location)
                   pygame.display.flip()

            elif event.key == pygame.K_LEFT:
                if soldier_location[0] != 0:
                    soldier_location[0] -= consts.PIXEL_PER_BLOCK_COL
                    screen.solider_draw(soldier_location)
                    pygame.display.flip()

            elif event.key == pygame.K_DOWN:
                if soldier_location[1] != consts.SCREEN_HEIGHT:
                    soldier_location[1] += consts.PIXEL_PER_BLOCK_ROW
                    screen.solider_draw(soldier_location)
                    pygame.display.flip()

            elif event.key == pygame.K_UP:
                if soldier_location[1] != 0:
                    soldier_location[1] -= consts.PIXEL_PER_BLOCK_ROW
                    screen.solider_draw(soldier_location)
                    pygame.display.flip()

    return game,soldier_location



if __name__ == "__main__":
    main()


