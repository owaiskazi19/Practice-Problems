

def can_partition(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False
    s = s / 2
    dp = [[False for x in range(s+1)]for y in range(len(nums))]
    
    for i in range(0, len(nums)):
        dp[i][0] =  True
    
    for j in range(1, s+1):
        dp[0][j] =  nums[0] == j 
    
    for i in range(1, len(nums)):
        for j in range(1 , s + 1):
            
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
    return dp[i-1][s]













def main():
  print "Can partition: " + str(can_partition([1, 2, 3, 4]))
  print "Can partition: " + str(can_partition([1, 1, 3, 4, 7])) 
  print "Can partition: " + str(can_partition([2, 3, 4, 6])) 


main()