import heapq

class Node:
    def __init__(self, x, y, cost, heuristic):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        # Custom comparison method for heapq
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(grid, start, goal):
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # Set to keep track of visited nodes
    visited = set()

    # Priority queue (heap) to store nodes based on their cost + heuristic
    heap = [Node(start[0], start[1], 0, 0)]

    # A* algorithm loop
    while heap:
        # Pop the node with the lowest cost + heuristic
        current = heapq.heappop(heap)

        # Skip if the node has already been visited
        if (current.x, current.y) in visited:
            continue

        # Mark the current node as visited
        visited.add((current.x, current.y))

        # Check if the current node is the goal
        if (current.x, current.y) == goal:
            return current.cost  # Return the cost when the goal is reached

        # Define the possible neighbors (up, down, left, right)
        neighbors = [(current.x + 1, current.y), (current.x - 1, current.y),
                     (current.x, current.y + 1), (current.x, current.y - 1)]

        # Iterate through neighbors
        for neighbor_x, neighbor_y in neighbors:
            # Check if the neighbor is within the grid boundaries and not an obstacle (1)
            if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols and grid[neighbor_x][neighbor_y] != 1:
                # Create a new node for the neighbor with updated cost and heuristic
                neighbor = Node(neighbor_x, neighbor_y, current.cost + 1, manhattan_distance((neighbor_x, neighbor_y), goal))

                # Add the neighbor to the priority queue
                heapq.heappush(heap, neighbor)

    return -1  # No path found

def manhattan_distance(point1, point2):
    # Calculate Manhattan distance between two points
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

result = astar(grid, start, goal)

if result != -1:
    print(f"Shortest path cost: {result}")
else:
    print("No path found.")