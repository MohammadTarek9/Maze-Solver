def heuristic(node, goal):
    pass

def a_star(graph, start, goal):

    pass

def reconstruct_path(came_from, current):

    pass


# Example Test Cases
def test_a_star():
    pass


def visualize_path():
    pass 


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
