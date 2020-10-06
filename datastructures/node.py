import pygame
from datastructures.color import Color


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = Color.WHITE.value
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def __lt__(self, other):
        return False

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == Color.RED.value

    def is_open(self):
        return self.color == Color.GREEN.value

    def is_barrier(self):
        return self.color == Color.BLACK.value

    def is_start(self):
        return self.color == Color.ORANGE.value

    def is_end(self):
        return self.color == Color.TURQUOISE.value

    def reset(self):
        self.color = Color.WHITE.value

    def make_start(self):
        self.color = Color.ORANGE.value

    def make_closed(self):
        self.color = Color.RED.value

    def make_open(self):
        self.color = Color.GREEN.value

    def make_barrier(self):
        self.color = Color.BLACK.value

    def make_end(self):
        self.color = Color.TURQUOISE.value

    def make_path(self):
        self.color = Color.PURPLE.value

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])
