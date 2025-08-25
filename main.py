import pygame
import screen
import consts
import sys

def main():
    game=True
    pygame.init()
    grass=screen.grass()
    screen.background_normal(grass)
    pygame.display.flip()
    while game:
        handle_user_event(game)

def handle_user_event(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ENTER:
                screen.draw_matrix_screen()
                pygame.time.wait(1000)


            if event.key == pygame.K_RIGHT:
               if consts.X_LOCATION != consts.MAT_COL - 1:
                   consts.X_LOCATION += 1

            elif event.key == pygame.K_LEFT:
                if consts.X_LOCATION != 0:
                    consts.X_LOCATION -= 1

            elif event.key == pygame.K_DOWN:
                if consts.Y_LOCATION != consts.MAT_ROW - 1:
                    consts.Y_LOCATION += 1

            elif event.key == pygame.K_UP:
                if consts.Y_LOCATION != 0:
                    consts.Y_LOCATION -= 1

    return game



if __name__ == "__main__":
    main()


