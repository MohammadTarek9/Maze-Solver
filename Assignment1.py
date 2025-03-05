import heapq as heap
import pygame
def heuristic(node, goal):
    # manhattan distance
    diff_x = abs(node[0] - goal[0])
    diff_y = abs(node[1] - goal[1])
    return diff_x + diff_y

def a_star(graph, start, goal):

    shortestPath = []
    totalCost = 0
    openList = []
    heuristic_start = heuristic(start, goal)
    heap.heappush(openList, (heuristic_start, start))
    cameFrom = {}
    accumulated_costs = {start: 0}
    while openList:
        current_heuristic, current = heap.heappop(openList)
        if current == goal:
            totalCost = accumulated_costs[current]
            shortestPath = reconstruct_path(cameFrom, current)
            return shortestPath, totalCost
        for neighbor in graph[current]:
            cell = (neighbor[0], neighbor[1])
            cost = neighbor[2]
            new_cost = accumulated_costs[current] + cost
            if cell not in accumulated_costs or new_cost < accumulated_costs[cell]:
                accumulated_costs[cell] = new_cost
                heap.heappush(openList, (new_cost + heuristic(cell, goal), cell))
                cameFrom[cell] = current
    return [], -1

            

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    path.reverse()
    return path

# Example Test Cases
def test_a_star():
    # test case 1
    maze = create_maze(50, 50, 0.2, 0)
    graph = create_graph(maze)
    start = (0, 0)
    goal = (49, 49)
    path, cost = a_star(graph, start, goal)
    print(f"Path of 1st test case: {path}")
    print(f"Cost of 1st test case: {cost}")
    visualize_path(graph, maze, start, goal, path)
    #test case 2
    maze = create_maze(60, 60, 0.1, 0.3)    
    graph = create_graph(maze)
    start = (0, 0)
    goal = (59, 59)
    path, cost = a_star(graph, start, goal)
    print(f"Path of 2nd test case: {path}")
    print(f"Cost of 2nd test case: {cost}")
    visualize_path(graph, maze, start, goal, path)
    #test case 3
    maze = create_maze(50, 50, 0.3, 0.5)
    graph = create_graph(maze)
    start = (0, 0)
    goal = (49, 49)
    path, cost = a_star(graph, start, goal)
    print(f"Path of 3rd test case: {path}")
    print(f"Cost of 3rd test case: {cost}")
    visualize_path(graph, maze, start, goal, path)


def visualize_path(graph, maze, start, goal, path):
    
    pygame.init()
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    pygame.display.set_caption("A* Pathfinding")
    clock = pygame.time.Clock()
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    
    cell_size = 12
    
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = WHITE if cell != '#' else BLACK
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
            
    for i, (x, y) in enumerate(path):
        pygame.draw.rect(screen, BLUE, (x * cell_size, y * cell_size, cell_size, cell_size))
        pygame.display.flip()
        clock.tick(20)
        
    pygame.draw.rect(screen, GREEN, (start[0] * cell_size, start[1] * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, RED, (goal[0] * cell_size, goal[1] * cell_size, cell_size, cell_size))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    pygame.quit()


import random

def create_maze(width, height, obstacle_percentage=0.2, weighted_percentage=0.1, seed=42):
    random.seed(seed)
    
    maze = []
    
    for i in range(height):
        row = []
        for j in range(width):
            # Randomly decide if the cell is an obstacle
            if random.random() < obstacle_percentage:
                row.append('#')  # Obstacle
            else:
                # Randomly assign weighted paths
                if random.random() < weighted_percentage:
                    row.append(random.randint(2, 5))  # Weighted path
                else:
                    row.append(1)  # Normal path with cost 1
        maze.append(row)
    
    return maze


def print_maze(maze):
    for row in maze:
        print(' '.join(str(cell) for cell in row))


def get_neighbors(x, y, maze):
    neighbors = []
    height = len(maze)
    width = len(maze[0])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] != '#':
            neighbors.append((nx, ny, maze[ny][nx]))
    
    return neighbors


def create_graph(maze):
    graph = {}
    
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] != '#':  # If the cell is not an obstacle
                graph[(x, y)] = get_neighbors(x, y, maze)
    
    return graph


def print_graph(graph):
    for node, neighbors in graph.items():
        print(f"Cell {node}: {neighbors}")


# Example: Create a 50x50 maze and build the graph
maze = create_maze(50, 50)
graph = create_graph(maze)

print_maze(maze)
# Print part of the graph to verify the structure
print_graph(graph)

# Test the A* algorithm
start = (0, 0)
goal = (49, 49)
path, cost = a_star(graph, start, goal)
print(f"Path of given graph: {path}")
print(f"Cost of given graph: {cost}")
visualize_path(graph, maze, start, goal, path)

test_a_star()
