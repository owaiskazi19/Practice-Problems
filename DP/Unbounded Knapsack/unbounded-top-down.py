

def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return check_knapsack(dp, profits, weights, capacity, 0)

def check_knapsack(dp, profits, weights, capacity, index):
    n = len(profits)

    if len(weights) != len(profits) or n == 0 or capacity <= 0 or index >= n:
        return 0
    
    if dp[index][capacity] == -1:
        profit1 = 0
        if weights[index] <= capacity:
            profit1 = profits[index] + check_knapsack(dp, profits, weights, capacity - weights[index], index)
        profit2 = check_knapsack(dp, profits, weights, capacity, index + 1)

        dp[index][capacity] = max(profit1, profit2)
    
    return dp[index][capacity]




def main():
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()