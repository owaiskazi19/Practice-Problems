def count_ways(n):
    dp = [0 for x in range(n+1)]
    return check_stairs(dp, n)

def check_stairs(dp, n):

    if n == 0:
        return 1
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    

    if dp[n] > 0:
        return dp[n]

    if dp[n] == 0:
        first_step = check_stairs(dp, n - 1)
        second_step = check_stairs(dp, n - 3)
        third_step = check_stairs(dp, n- 4)

        dp[n] = first_step + second_step + third_step
    
    return dp[n]

def main():

  print(count_ways(4))
  print(count_ways(5))
  print(count_ways(6))


main()