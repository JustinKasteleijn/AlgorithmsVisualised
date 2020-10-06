import pygame
from astar.node import Node
from astar.color import Color


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, Color.GREY.value, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, Color.GREY.value, (j * gap, 0), (j * gap, width))


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col
