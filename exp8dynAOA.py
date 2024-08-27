def write(x):
    subset = []
    for i in range(len(x)):
        subset.append(x[i])
    print(tuple(subset))

def sum_of_subsets(s, k, r, x, w, m, n):
    x[k] = 1
    if s + w[k] == m:
        write(x)
        for i in range(k, n):
            x[i] = 0
    elif s + w[k] + w[k + 1] <= m:
        sum_of_subsets(s + w[k], k + 1, r - w[k], x, w, m, n)
    if s + r - w[k] >= m and s + w[k + 1] <= m:
        x[k] = 0
        sum_of_subsets(s, k + 1, r - w[k], x, w, m, n)

def main():
    total = 0
    n = int(input("Enter the number of elements: "))
    w = []
    x = []
    print("Enter the elements: ", end="")
    for _ in range(n):              
        w.append(int(input()))
        x.append(0)
    m = int(input("Enter the target sum: "))
    total = sum(w)
    print("The subsets are:")
    sum_of_subsets(0, 0, total, x, w, m, n)

if __name__ == "__main__":
    main()      