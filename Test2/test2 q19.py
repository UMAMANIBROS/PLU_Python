#19.Perform a Breadth-First Search (BFS) traversal starting from vertex A.
from collections import deque
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
