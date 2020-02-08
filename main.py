import pygame
from game.game_manager import GameManager

BACKGROUND = (23,23,45)

def setup(caption='Hello', width=800, height=600, background=(23,23,45)):
    pygame.init()
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode((width, height))
    screen.fill(background)

    return screen

def draw(root):
    running = True

    game = GameManager(root)

    # Main loop
    while running:
        root.fill(BACKGROUND)
        game.draw_map()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

if __name__ == '__main__':
    root = setup()
    draw(root)
