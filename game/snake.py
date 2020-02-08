import pygame
from enum import Enum
from collections import namedtuple

dirs = Enum('_dir', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
_walk = namedtuple('Walk', 'up down left right')

class Snake():
    alive = True
    body_size = 20
    pace = body_size
    body = []
    color = (200,200,200)
    walk = _walk(up=(0,-1), down=(0,1), left=(-1,0), right=(1,0))
    curr_dir = walk.right


    def __init__(self, root, pos, res=20):
        self.root = root
        self.body.append(pos)
        self.body_size = res
        self.pace = res

    def update(self, dt, events):
        for event in events:
            if event.key == pygame.K_RIGHT and self.curr_dir != self.walk.left:
                self.curr_dir = self.walk.right
            elif event.key == pygame.K_LEFT and self.curr_dir != self.walk.right:
                self.curr_dir = self.walk.left
            elif event.key == pygame.K_UP and self.curr_dir != self.walk.down:
                self.curr_dir = self.walk.up
            elif event.key == pygame.K_DOWN and self.curr_dir != self.walk.up:
                self.curr_dir = self.walk.down
            elif event.key == pygame.K_SPACE:
                self.grow()

        if self.alive:
            self.move()

    def move(self):
        width, height = self.root.get_size()
        pos = self.body[-1]
        if (pos[0] >= 0 and (pos[0] + self.body_size) <= width) and (pos[1] >= 0 and (pos[1] + self.body_size) <= height):
            dx, dy = tuple(self.pace*i for i in self.curr_dir)
            curr_head = self.body[-1]
            piece = self.body.pop(0)
            new_head = self.body[-1] if self.body else piece
            new_head = (new_head[0] + dx, new_head[1] + dy)
            self.body.append(new_head)
        else:
            self.alive = False

    def grow(self):
        dx, dy = tuple(self.pace*i for i in self.curr_dir)
        piece = (self.body[-1][0] + dx, self.body[-1][1] + dy)
        self.body.append(piece)

    def draw(self):
        for piece in self.body:
            rect = (*piece, self.body_size, self.body_size)
            pygame.draw.rect(self.root, self.color, rect)

    def eat(self):
        pass