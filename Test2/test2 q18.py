#18.Check whether there is a direct edge between two given vertices
# Create Graph
graph = {}
graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "D"]
graph["D"] = ["B", "C"]
v1 = input("Enter First Vertex: ")
v2 = input("Enter Second Vertex: ")
if v2 in graph[v1]:
    print("Direct Edge Exists")
else:
    print("Direct Edge Does Not Exist")