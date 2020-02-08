import pygame
from game.snake import Snake
from random import randint

class GameManager():
    game_over = False
    food = None

    def __init__(self, root, res=20):
        self.root = root
        width, height =  self.root.get_size()
        self.cols = int(width/res)
        self.rows = int(height/res)
        self.res = res

        self.gen_food()

        self.player = Snake(self.root, (400,300), res=self.res)

    def gen_food(self):
        fx = randint(0, self.cols - 1)
        fy = randint(0, self.rows - 1)
        self.food = pygame.Rect(fx * self.res, fy * self.res, self.res, self.res)

    def draw_food(self):
        if self.food:
            food_color = (200, 34, 34)
            pygame.draw.rect(self.root, food_color, self.food)

    def _draw_map(self):
        cell_color = (200,200,200, 10)
        for row in range(self.rows):
            for col in range(self.cols):
                cell = pygame.Rect(col * self.res, row * self.res, self.res, self.res)
                pygame.draw.rect(self.root, cell_color, cell, 1)

    def update(self, dt, events):
        self.player.update(dt, events)
        head = self.player.body[-1]
        if head.colliderect(self.food):
            self.player.grow()
            self.gen_food()

    def draw(self):
        # self._draw_map()
        self.draw_food()
        self.player.draw()
