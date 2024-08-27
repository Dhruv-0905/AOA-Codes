import heapq

def prim(graph):
    # Initialize variables
    visited = set()
    start_node = list(graph.keys())[0]
    min_heap = [(0, start_node, None)]
    mst = []

    while min_heap:
        cost, current_node, parent = heapq.heappop(min_heap)

        if current_node not in visited:
            visited.add(current_node)
            if parent is not None:
                mst.append((parent, current_node, cost))

            for neighbor, neighbor_cost in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor_cost, neighbor, current_node))

    return mst

def kruskal(graph):
    # Initialize variables
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            edges.append((weight, vertex, neighbor))

    edges.sort()  # Sort edges by weight
    parent = {vertex: vertex for vertex in graph}

    def find_set(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find_set(parent[vertex])
        return parent[vertex]

    def union(u, v):
        root_u = find_set(u)
        root_v = find_set(v)
        parent[root_u] = root_v

    mst = []

    for edge in edges:
        weight, u, v = edge
        if find_set(u) != find_set(v):
            mst.append((u, v, weight))
            union(u, v)

    return mst

def main():
    # Input graph from the user
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    print("Enter edges and their weights (vertex1 vertex2 weight):")
    for _ in range(edges):
        edge_info = input().split()
        vertex1, vertex2, weight = map(int, edge_info)

        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []

        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))

    # Run Prim's algorithm
    minimum_spanning_tree_prim = prim(graph.copy())

    # Run Kruskal's algorithm
    minimum_spanning_tree_kruskal = kruskal(graph.copy())

    # Display the minimum spanning trees and their costs
    print("\nMinimum Spanning Tree using Prim's algorithm:")
    total_cost_prim = 0
    for edge in minimum_spanning_tree_prim:
        print(f"Edge: {edge[0]} - {edge[1]}, Cost: {edge[2]}")
        total_cost_prim += edge[2]
    print(f"Total Cost of Minimum Spanning Tree (Prim): {total_cost_prim}")

    print("\nMinimum Spanning Tree using Kruskal's algorithm:")
    total_cost_kruskal = 0
    for edge in minimum_spanning_tree_kruskal:
        print(f"Edge: {edge[0]} - {edge[1]}, Cost: {edge[2]}")
        total_cost_kruskal += edge[2]
    print(f"Total Cost of Minimum Spanning Tree (Kruskal): {total_cost_kruskal}")

if __name__ == "__main__":
    main()
