import pygame


class Button:
    def __init__(self, x, y, size_x, size_y):
        self.index = 0
        self.algorithms = ["dijkstra", "astar"]
        self.button = pygame.Rect(x, y, size_x, size_y)

    def is_clicked(self, mousePos):
        return self.button.collidepoint(mousePos)

    def draw_button(self, screen, color):
        pygame.draw.rect(screen, color, self.button)

    def get_algorithm(self, pos):
        return self.algorithms[pos]

    def get_size(self):
        return len(self.algorithms)
