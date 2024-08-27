def knapsack(weights, values, capacity):
    n = len(weights)
    # Initialize a table to store the maximum values that can be obtained for each capacity and item count
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the table using dynamic programming
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Trace back to find the selected items 
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected_items[::-1]

def knapsack_main():
    n = int(input("Enter the number of items: "))
    weights = []
    values = []
    print("Enter the weights of the items:")
    for _ in range(n):
        weights.append(int(input()))
    print("Enter the values of the items:")
    for _ in range(n):
        values.append(int(input()))
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    max_value, selected_items = knapsack(weights, values, capacity)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)

# Example usage:
knapsack_main()
