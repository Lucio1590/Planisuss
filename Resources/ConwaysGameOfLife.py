import time
import pygame
import numpy as np

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

PREYS = (0, 255, 0)
PREDATORS = (255, 0, 0)
WATER = (0, 0, 255)



class Cell:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.type  = "Cell"

    def __str__(self):
        return "Cell at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __repr__(self):
        return "Cell at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.alive == other.alive

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y, self.alive))

class Vegetob(Cell):
    def __init__(self, x, y, alive):
        super().__init__(x, y, alive)
        self.type = "Vegetob"

    def __str__(self):
        return "Vegetob at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __repr__(self):
        return "Vegetob at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead") 

class Erbast(Cell):
    def __init__(self, x, y, alive):
        super().__init__(x, y, alive)
        self.type = "Erbast"

    def __str__(self):
        return "Erbast at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __repr__(self):
        return "Erbast at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

class Carviz(Cell):
    def __init__(self, x, y, alive):
        super().__init__(x, y, alive)
        self.type = "Carviz"

    def __str__(self):
        return "Carviz at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __repr__(self):
        return "Carviz at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

def update(screen, cells, size, with_progress = False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = BLACK if cells[row, col] == 0 else WHITE
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = GRAY
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = WHITE
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = WHITE

        pygame.draw.rect(screen, color, [size*col, size*row, size-1, size-1])

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Conway's Game of Life")

    cells = np.zeros((60, 80))
    #cells have to be objects
    #cells = np.zeros((60, 80), dtype=object)

    screen.fill(GRAY)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                elif event.key == pygame.K_r:
                    running = False
                    cells = np.zeros((60, 80))
                    screen.fill(GRAY)
                    update(screen, cells, 10)
                    pygame.display.flip()
                    pygame.display.update()
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col = pos[0] // 10
                row = pos[1] // 10
                # make sure we are in the bounds of the array
                if row >= cells.shape[0] or col >= cells.shape[1]:
                    continue
                cells[row, col] = 1 if cells[row, col] == 0 else 0
                color = WHITE if cells[row, col] == 1 else BLACK
                pygame.draw.rect(screen, color, [col*10, row*10, 9, 9])
                pygame.display.flip()
                pygame.display.update()

        if running:
            cells = update(screen, cells, 10, True)
            pygame.display.flip()
            pygame.display.update()
            time.sleep(0.01)
if __name__ == '__main__':
    main()