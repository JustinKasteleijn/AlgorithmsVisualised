from astar.a_star import astar
from astar.dijkstra import dijkstra
from datastructures.grid import *
from datastructures.button import Button

WIDTH = 700
TOP_LAYER = 100
WIN = pygame.display.set_mode((WIDTH, TOP_LAYER + WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


def draw(win, grid, rows, width, button):
    win.fill(Color.WHITE.value)
    button.draw_button(WIN, Color.TURQUOISE.value)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def main(win, width):
    rows = 50
    grid = make_grid(rows, width)
    start = None
    end = None
    run = True
    button = Button(250, 725, 175, 50)

    while run:
        draw(win, grid, rows, width, button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if button.is_clicked(pygame.mouse.get_pos()):
                if button.index == button.get_size():
                    button.index -= 1
                button.index += 1
                print("Hallo")

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pos()[1] < WIDTH:
                    row, col = get_clicked_pos(pos, rows, width)
                    node = grid[row][col]
                    if not start and node != end:
                        start = node
                        start.make_start()

                    elif not end and node != start:
                        end = node
                        end.make_end()

                    elif node != end and node != start:
                        node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    astar(lambda: draw(win, grid, rows, width, button), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(rows, width)

    pygame.quit()


main(WIN, WIDTH)
