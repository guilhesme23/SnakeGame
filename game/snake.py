import pygame
from enum import Enum
from collections import namedtuple

dirs = Enum('_dir', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
_walk = namedtuple('Walk', 'up down left right')

class Snake():
    alive = True
    points = 5
    body_size = 15
    pace = 0.5
    pos = (0,0)
    body = []
    color = (200,200,200)
    walk = _walk(up=(0,-1), down=(0,1), left=(-1,0), right=(1,0))
    curr_dir = walk.up


    def __init__(self, root, pos):
        self.pos = pos
        self.root = root
        self.body.append(self.pos)

    def update(self):
        keys = pygame.key.get_pressed()
        move_keys = keys[273:277]
        if keys[275]:
            self.curr_dir = self.walk.right
        elif keys[276]:
            self.curr_dir = self.walk.left
        elif keys[273]:
            self.curr_dir = self.walk.up
        elif keys[274]:
            self.curr_dir = self.walk.down
        elif keys[pygame.K_SPACE]:
            self.grow()

        if self.alive:
            self.move()

    def move(self):
        width, height = self.root.get_size()
        pos = self.body[0]
        if (pos[0] >= 0 and (pos[0] + self.body_size) <= width) and (pos[1] >= 0 and (pos[1] + self.body_size) <= height):
            dx, dy = tuple(self.pace*i for i in self.curr_dir)
            self.pos = self.body[-1]
            for i, piece in enumerate(self.body):
                self.body[i] = (piece[0] + dx, piece[1] + dy)
        else:
            self.body[0] = (400,300)
            self.alive = False

    def grow(self):
        last_pos = self.pos
        grow_dir = [-self.pace * i for i in self.curr_dir]
        new_pos = (grow_dir[0] + last_pos[0], grow_dir[1] + last_pos[1])
        self.body.append(self.pos)

    def draw(self):
        for piece in self.body:
            rect = (*piece, self.body_size, self.body_size)
            pygame.draw.rect(self.root, self.color, rect)

    def eat(self):
        pass