import pygame

def main():
    pygame.init()

def key_control ():
    key_input = input()
    check = pygame.key.get_focused(key_input)
    if check:
        pygame.key.get_mods(key_input)


if __name__ == "__main__":
    main()


