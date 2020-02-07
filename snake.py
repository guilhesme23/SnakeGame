import pygame
from enum import Enum
from collections import namedtuple

dirs = Enum('_dir', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
_walk = namedtuple('Walk', 'up down left right')

class Snake():
    alive = True
    points = 5
    body_size = 15
    pace = 5
    pos = (0,0)
    body = []
    color = (200,200,200)
    curr_dir = dirs.UP
    walk = _walk(up=(0,-pace), down=(0,pace), left=(-pace,0), right=(pace,0))


    def __init__(self, root, pos):
        self.pos = pos
        self.root = root
        self.body.append(self.pos)

    def update(self):
        pass

    def draw(self):
        for piece in self.body:
            rect = (*piece, self.body_size, self.body_size)
            pygame.draw.rect(self.root, self.color, rect)

    def eat(self):
        pass