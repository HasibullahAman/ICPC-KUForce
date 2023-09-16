
# Function to find the parent of a node in the disjoint set
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Function to perform union of two sets
def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    parent[x_root] = y_root

# Function to find the minimum cost of connecting all points
def minimum_cost(points, connections):
    parent = [i for i in range(points)]
    total_cost = 0

    # Sort connections based on their cost in ascending order
    connections.sort(key=lambda x: x[2])

    for connection in connections:
        x = find(parent, connection[0])
        y = find(parent, connection[1])

        if x != y:
            total_cost += connection[2]
            union(parent, [], x, y)

    return total_cost

# Iterate through each test case
for _ in range(int(input())):
    # Read the number of points and connections
    points, connections = map(int, input().split())

    # Read the connection details
    connection_list = []
    for _ in range(connections):
        connection = list(map(int, input().split()))
        connection_list.append(connection)

    # Find the minimum cost for the current test case
    min_cost = minimum_cost(points, connection_list)

    # Print the minimum cost
    print(min_cost)
