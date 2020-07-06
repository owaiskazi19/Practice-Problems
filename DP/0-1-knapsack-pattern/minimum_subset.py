
def can_partition(nums):
    s = sum(nums)
    n = len(nums)

    dp = [[False for x in range(int(s/2)+1)] for y in range(n)]

    for i in range(0,n):
        dp[i][0] = True
    
    for j in range(0, int(s/2)+1):
        dp[0][j] = nums[0] == j
    
    for i in range(1, n):
        for j in range(1, int(s/2)+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
    
    sum1 = 0

    for i in range(int(s/2), -1, -1):
        if dp[n-1][i]:
    
            sum1 = i
            break
    
    sum2 = s - sum1

    return abs(sum1-sum2)






def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()