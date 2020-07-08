
def count_ribbon_pieces(ribbons, total):
    dp = [[-1 for x in range(total+1)] for y in range(len(ribbons))]
    res = check_ribbon(dp, ribbons, total, 0)
    return -1 if res == -float('inf') else res

def check_ribbon(dp, ribbons, total, index):
    if total == 0:
        return 0
    n = len(ribbons)
    if n == 0 or index >= n:
        return -float('inf')
    
    if dp[index][total] != -1:
        return dp[index][total]
    
    c1 = -float('inf')
    if ribbons[index] <= total:
        res = check_ribbon(dp, ribbons, total - ribbons[index], index)
        if res != -float('inf'):
            c1 = res + 1
    c2 = check_ribbon(dp, ribbons, total, index + 1)

    dp[index][total] = max(c1, c2)
    return dp[index][total]















def main():
  print(count_ribbon_pieces([2, 3, 5], 5))
  print(count_ribbon_pieces([2, 3], 7))
  print(count_ribbon_pieces([3, 5, 7], 13))
  print(count_ribbon_pieces([3, 5], 7))


main()