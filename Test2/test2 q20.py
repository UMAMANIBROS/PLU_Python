#20.Perform a Depth-First Search (DFS) traversal starting from vertex A.
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
visited = []