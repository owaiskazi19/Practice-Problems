def find_max_steal(wealth):
    dp = [0 for x in range(len(wealth))]
    return check_welth(dp, wealth, 0)

def check_welth(dp, wealth, index):
    n = len(wealth)

    if index >= n:
        return 0
    
    if dp[index] == 0:
        st1 = wealth[index] + check_welth(dp, wealth, index + 2)
        st2 = check_welth(dp, wealth, index + 1)

        dp[index] = max(st1, st2)
    
    return dp[index]











def main():

  print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
  print(find_max_steal([2, 10, 14, 8, 1]))


main()