import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}
        for i in range(vertices):
            self.graph[i] = {}

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def dijkstra(self, start):
        visited = [False] * self.vertices
        distance = [sys.maxsize] * self.vertices
        predecessor = [-1] * self.vertices  # To store the predecessor of each vertex in the shortest path
        distance[start] = 0

        for _ in range(self.vertices):
            min_distance = sys.maxsize
            min_index = -1

            for v in range(self.vertices):
                if not visited[v] and distance[v] < min_distance:
                    min_distance = distance[v]
                    min_index = v

            visited[min_index] = True

            for neighbor, weight in self.graph[min_index].items():
                if not visited[neighbor] and distance[min_index] + weight < distance[neighbor]:
                    distance[neighbor] = distance[min_index] + weight
                    predecessor[neighbor] = min_index

        return distance, predecessor

def print_path(predecessor, current_vertex):
    if predecessor[current_vertex] == -1:
        print(current_vertex, end=" ")
        return
    print_path(predecessor, predecessor[current_vertex])
    print(current_vertex, end=" ")

def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    graph = Graph(vertices)

    for _ in range(edges):
        u, v, weight = map(int, input("Enter edge (u v weight): ").split())
        graph.add_edge(u, v, weight)

    start_vertex = int(input("Enter the starting vertex: "))

    shortest_paths, predecessors = graph.dijkstra(start_vertex)

    print("\nShortest paths from vertex", start_vertex)
    for i, distance in enumerate(shortest_paths):
        print(f"To vertex {i}: {distance}, Path: ", end="")
        print_path(predecessors, i)
        print()

if __name__ == "__main__":
    main()