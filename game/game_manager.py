import pygame
import numpy as np

class GameManager():
    game_over = False

    def __init__(self, root, res=20):
        self.root = root
        width, height =  self.root.get_size()
        self.cols = int(width/res)
        self.rows = int(height/res)
        self.res = res

    def draw_map(self):
        cell_color = (200,200,200,90)
        for row in range(self.rows):
            for col in range(self.cols):
                cell = pygame.Rect(col * self.res, row * self.res, self.res, self.res)
                pygame.draw.rect(self.root, cell_color, cell, 1)

