def can_partition(nums, s):
    n = len(nums)
    dp = [[False for x in range(s+1)] for y in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    for j in range(1, s+1):
        dp[0][j] = True if nums[0] == j else False

    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
    
    return dp[i-1][s]









def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()