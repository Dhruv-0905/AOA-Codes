def next_value(n, m, x, k, G):
    for i in range(n):
        if x[i] > m:
            m = x[i]

    while True:
        x[k] = (x[k] + 1) % (m + 1)
        if x[k] == 0:
            return
        for j in range(n):
            if G[k][j] and x[k] == x[j]:
                break
        if j == n - 1:
            return

def write(n, x):
    for i in range(n):
        print(x[i], end=" ")
    print()

def graph_coloring(n, m, x, k, G):
    while True:
        next_value(n, m, x, k, G)
        if x[k] == 0:
            return
        elif k == n - 1:
            write(n, x)
        else:
            graph_coloring(n, m, x, k + 1, G)

def main():
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the maximum number of colors: "))
    G = []  
    print("Enter the adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        G.append(row)
    x = [0] * n
    print("The possible solutions are:")
    graph_coloring(n, m, x, 0, G)

if __name__ == "__main__":
    main()