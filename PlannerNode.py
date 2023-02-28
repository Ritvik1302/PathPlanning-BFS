import sys

import self as self

from MapNode import MapNode
from queue import Queue
from collections import deque


def bfs(maze, start, goal):
    # Set up the starting node and the queue
    queue = deque()
    visited = set()
    queue.append(start)

    # Set up the parent dictionary to keep track of the path
    parent = {start: None}

    # Start the BFS algorithm
    while queue:
        current = queue.popleft()

        if current == goal:
            # We have found the goal, so we can return the path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        visited.add(current)

        # Get the neighbors of the current node
        neighbors = get_neighbors(maze, current)

        for neighbor in neighbors:
            if neighbor not in visited:
                parent[neighbor] = current
                queue.append(neighbor)

    # We have searched the entire maze and have not found the goal
    return None


def get_neighbors(maze, current):
    neighbors = []
    rows, cols = len(maze), len(maze[0])
    x, y = current

    # Check north
    if x > 0 and not (maze[x][y] & 8):
        neighbors.append((x - 1, y))

    # Check south
    if x < rows - 1 and not (maze[x][y] & 1):
        neighbors.append((x + 1, y))

    # Check west
    if y > 0 and not (maze[x][y] & 4):
        neighbors.append((x, y - 1))

    # Check east
    if y < cols - 1 and not (maze[x][y] & 2):
        neighbors.append((x, y + 1))

    return neighbors


class PlannerNode:

    def __init__(self):
        self.current_obj = MapNode()
        # Since we know that the first step the bot will take will be down, we can simply do it here
        # self.current_obj.direction_callback("down")  # example 1
        # self.wall_callback()

        path = bfs(self.current_obj.array, self.current_obj.walls.start, self.current_obj.walls.end)

        for i in range(len(path) - 1):
            curr_x, curr_y = path[i]
            next_x, next_y = path[i + 1]

            if curr_x < next_x:
                self.current_obj.direction_callback("down")
            elif curr_x > next_x:
                self.current_obj.direction_callback("up")
            elif curr_y < next_y:
                self.current_obj.direction_callback("right")
            elif curr_y > next_y:
                self.current_obj.direction_callback("left")

    def wall_callback(self):
        # current_obj has all the attributes to help you in your path planning !

        pass  # Your code goes here. You need to figure out an algorithm to decide on the best direction of movement
        # of the bot based on the data you have.
        # after deciding on the direction, you need to call the direction_callback() function as done in example 1.


if __name__ == '__main__':
    start_obj = PlannerNode()
    start_obj.current_obj.print_root.mainloop()
