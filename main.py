import pygame
from game.game_manager import GameManager

BACKGROUND = (23,23,45)

def setup(caption='Hello', width=800, height=600, background=(23,23,45)):
    pygame.init()
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode((width, height))
    screen.fill(background)

    pygame.font.init()
    return screen

def draw(root):
    running = True

    game = GameManager(root, 10)
    getTicksLastFrame = 0
    clock = pygame.time.Clock()
    # Main loop
    while running:
        root.fill(BACKGROUND)
        dt = clock.tick(12)
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                events.append(event)

        game.update(dt, events)
        game.draw()

        pygame.display.update()

if __name__ == '__main__':
    root = setup()
    draw(root)
