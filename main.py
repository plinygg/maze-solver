import pygame
from random import choice
from collections import deque
from mazegenerator import * 

RES = WIDTH, HEIGHT = 725, 725
TILE = 50
COLS, ROWS = WIDTH // TILE, HEIGHT // TILE

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

def bfs(root):
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        print(node.x, node.y)
        node.draw_current_cell()
        if node.end:
            return

        #need to somehow find a way to go node = node.next or something like that
        x, y = node.x, node.y
        if not node.walls['top']:
            if node.check_cell(x, y-1) and not node.bfsvisited:
                q.append(node.check_cell(x, y-1)) 
                node.bfsvisited = True
        if not node.walls['bottom']:
            if node.check_cell(x, y+1) and not node.bfsvisited:
                q.append(node.check_cell(x, y+1))
                node.bfsvisited = True
        if not node.walls['left']:
            if node.check_cell(x-1, y) and not node.bfsvisited:
                q.append(node.check_cell(x-1, y)) 
                node.bfsvisited = True
        if not node.walls['right']:
            if node.check_cell(x+1, y) and not node.bfsvisited:
                q.append(node.check_cell(x+1, y)) 
                node.bfsvisited = True
        


grid_cells = [Cell(col, row) for row in range(ROWS) for col in range(COLS)]
current_cell = grid_cells[0]
stack = []
maze = generate_maze()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    if keys[pygame.K_b]:
        bfs(grid_cells[0])
    if keys[pygame.K_w]:
       [cell.draw(screen) for cell in maze]

    screen.fill('gray')

    
    
    pygame.display.flip()
    dt = clock.tick(100)
