

def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)

def knapsack_recursive(dp ,profits, weights, capacity, index):

    if capacity <=0 or index >= len(profits):
        return 0
    
    if dp[index][capacity] != -1:
      return dp[index][capacity]
    # recursive call after choosing the element at the currentIndex
  # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit1 = 0
    if weights[index] <= capacity:
      profit1 = profits[index] + knapsack_recursive(
      dp, profits, weights, capacity - weights[index], index + 1)
    
      # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(
    dp, profits, weights, capacity, index + 1)

    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]




print solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)
print solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)