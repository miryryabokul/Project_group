import pygame
import screen


def main():
    pygame.init()
    screen.normal_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
    pygame.quit()



def key_control ():
    key_input = input()
    check = pygame.key.get_focused(key_input)
    if check:
        pygame.key.get_mods(key_input)


if __name__ == "__main__":
    main()


