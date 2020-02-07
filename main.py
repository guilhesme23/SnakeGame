import pygame
from snake import Snake

def setup(caption='Hello', width=800, height=600, background=(23,23,45)):
    pygame.init()
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode((width, height))
    screen.fill(background)

    return screen

def draw(root):
    running = True

    snake = Snake(root, (200,200))

    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        snake.draw()

        pygame.display.update()

if __name__ == '__main__':
    root = setup()
    draw(root)
