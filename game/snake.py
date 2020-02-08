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
        self.body_size = res
        self.pace = res
        rect = pygame.Rect(*pos, self.body_size, self.body_size)
        self.body = [rect]

    def update(self, dt, events):
        self.check_liveness()

        for event in events:
            if event.key == pygame.K_RIGHT and self.curr_dir != self.walk.left:
                self.curr_dir = self.walk.right
            elif event.key == pygame.K_LEFT and self.curr_dir != self.walk.right:
                self.curr_dir = self.walk.left
            elif event.key == pygame.K_UP and self.curr_dir != self.walk.down:
                self.curr_dir = self.walk.up
            elif event.key == pygame.K_DOWN and self.curr_dir != self.walk.up:
                self.curr_dir = self.walk.down

        if self.alive:
            self.move()

    def move(self):
        width, height = self.root.get_size()
        pos = self.body[-1]

        dx, dy = tuple(self.pace*i for i in self.curr_dir)
        curr_head = self.body[-1]
        piece = self.body.pop(0)
        new_head = self.body[-1] if self.body else piece
        new_head = pygame.Rect(new_head[0] + dx, new_head[1] + dy, self.body_size, self.body_size)
        self.body.append(new_head)

    def grow(self):
        dx, dy = tuple(self.pace*i for i in self.curr_dir)
        piece = (self.body[-1][0] + dx, self.body[-1][1] + dy)
        rect = pygame.Rect(*piece, self.body_size, self.body_size)
        self.body.append(rect)

    def draw(self):
        for piece in self.body:
            pygame.draw.rect(self.root, self.color, piece)

    def check_liveness(self):
        # Ways to die:
        # 1- Exit the world
        # 2- Eat your own tail
        hx, hy, *_ = self.body[-1]
        width, height = self.root.get_size()
        if (hx < 0 or (hx + self.body_size) > width) or (hy < 0 or (hy + self.body_size) > height):
            self.alive = False

        head = self.body[-1]
        for bod in self.body[:-1]:
            if head.colliderect(bod):
                self.alive = False
                break

        if not self.alive:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            wohoo = font.render('Game Over', False, self.color)
            self.root.blit(wohoo, (200, 400))

    def eat(self):
        pass