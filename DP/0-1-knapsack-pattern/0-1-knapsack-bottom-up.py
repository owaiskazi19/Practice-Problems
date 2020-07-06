
def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if n == 0 or capacity <=0 or len(weights) != n:
        return 0
    
    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    
    for i in range(1, n):
        for c in range(1, capacity+1):

            profit1, profit2 = 0 , 0

            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]

            profit2 = dp[i-1][c]

            dp[i][c] = max(profit1,profit2)

    return dp[n-1][capacity]














print solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)
print solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)