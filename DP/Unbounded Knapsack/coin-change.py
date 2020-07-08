def count_change(denominations, total):
    dp = [[-1 for x in range(total + 1)] for y in range(len(denominations))]
    return check_coins(dp, denominations, total, 0)

def check_coins(dp, denominations, total, index):
    n = len(denominations)
    if total == 0:
        return 1
    
    if n == 0 or index >= n:
        return 0
    
    if dp[index][total] != -1:
        return dp[index][total]
    
    sum1 = 0
    if denominations[index] <= total:
        sum1 = check_coins(dp, denominations, total - denominations[index], index)
    
    sum2 = check_coins(dp, denominations, total, index + 1)

    dp[index][total] = sum1 + sum2
    return dp[index][total]












def main():
  print(count_change([1, 2, 3], 5))


main()