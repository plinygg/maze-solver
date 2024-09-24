import pygame
from random import choice

RES = WIDTH, HEIGHT = 725, 725
TILE = 25
COLS, ROWS = WIDTH // TILE, HEIGHT // TILE

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

        
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {"top": True, "bottom": True, "right": True, "left": True}
        self.visited = False #has the cell been visited/unvisited
        self.end = False # if the cell is the end cell (when to end the search program)

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.end:
            pygame.draw.rect(screen, 'red', (x, y, TILE, TILE))
        if self.visited:
            pygame.draw.rect(screen, 'white', (x, y, TILE, TILE))

        if self.walls['top']:
            pygame.draw.line(screen, 'black', (x, y), (x + TILE, y), 2)
        if self.walls['right']:
            pygame.draw.line(screen, 'black', (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.walls['bottom']:
            pygame.draw.line(screen, 'black', (x + TILE, y + TILE), (x , y + TILE), 2)
        if self.walls['left']:
            pygame.draw.line(screen, 'black', (x, y + TILE), (x, y), 2)
    
    def draw_current_cell(self):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(screen, 'green', (x+2, y+2, TILE - 2, TILE - 2))
    
    def check_cell(self, x, y):
        if (x < 0 or x > COLS - 1 or y < 0 or y > ROWS - 1):
            return False

        i = x + y * COLS
        return grid_cells[i]
    
    def check_neighbors(self, grid_cells):
        self.grid_cells = grid_cells
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        bottom = self.check_cell(self.x, self.y + 1)
        right = self.check_cell(self.x + 1, self.y)
        left = self.check_cell(self.x - 1, self.y)

        if top and not top.visited:
            neighbors.append(top)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if right and not right.visited:
            neighbors.append(right)
        if left and not left.visited:
            neighbors.append(left)

        return choice(neighbors) if neighbors else False
    
def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False


grid_cells = [Cell(col, row) for row in range(ROWS) for col in range(COLS)]
current_cell = grid_cells[0]
stack = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False


    screen.fill('gray')
    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw_current_cell()

    next_cell = current_cell.check_neighbors(grid_cells)
    if next_cell:
        next_cell.visited = True
        remove_walls(current_cell, next_cell)
        current_cell = next_cell


    pygame.display.flip()
    dt = clock.tick(60)
