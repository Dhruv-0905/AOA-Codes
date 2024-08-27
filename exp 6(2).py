def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[""] * (n + 1) for _ in range(m + 1)]
    intermediate_states = []

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "\u2196"  # Unicode for diagonal arrow (NW)
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "\u2191"  # Unicode for upward arrow
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "\u2190"  # Unicode for leftward arrow
            
            # Append a copy of the current state
            intermediate_states.append((list(map(list, c)), list(map(list, b))))
            # Print the step
            print("Step:", i, j)
            print("Length array:")
            for row in c:
                print(row)
            print("Direction array:")
            for row in b:
                print(row)
            print()

    # Now, let's construct the LCS from the direction array
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if b[i][j] == "\u2196":  # Diagonal arrow
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == "\u2191":  # Upward arrow
            i -= 1
        else:  # Leftward arrow
            j -= 1

    return intermediate_states, ''.join(reversed(lcs))

def main():
    X = input("Enter the first string: ")
    Y = input("Enter the second string: ")
    intermediate_states, lcs = lcs_length(X, Y)
    print("\nIntermediate states:")
    for state in intermediate_states:
        c, b = state
        print("\nLength array:")
        for row in c:
            print(row)
        print("Direction array:")
        for row in b:
            print(row)
        print()

    print("\nLongest Common Subsequence (LCS):", lcs)

if __name__ == "__main__":
    main()
