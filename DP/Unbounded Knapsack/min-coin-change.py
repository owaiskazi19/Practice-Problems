import math

def count_change(denominations, total):
    dp = [[-1 for x in range(total+1)] for y in range(len(denominations))]
    res =  check_coin(dp, denominations, total, 0)
    return -1 if res == float('inf')  else res 


def check_coin(dp, denominations, total, index):
    if total == 0:
        return 0
    
    n = len(denominations)
    if n == 0 or index >= n:
        return float('inf') 
    
    if dp[index][total] != -1:
        return dp[index][total]

    count1 = float('inf') 
    if denominations[index] <= total:
        
        res = check_coin(dp, denominations, total - denominations[index], index)

        if res != float('inf') :
            count1 = res + 1
    
    count2 = check_coin(dp, denominations, total, index + 1)

    dp[index][total] = min(count1, count2)

    return dp[index][total]






def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()