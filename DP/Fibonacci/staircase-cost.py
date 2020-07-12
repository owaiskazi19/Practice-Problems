def find_min_fee(jumps):
    dp = [0 for x in range(len(jumps))]
    return check_fee(dp ,jumps, 0)

def check_fee(dp, jumps, index):
    n = len(jumps)
    if index > n - 1:
        return 0
    
    if dp[index] == 0:
        take1step = check_fee(dp, jumps, index + 1)
        take2step = check_fee(dp, jumps, index + 2)
        take3step = check_fee(dp, jumps, index + 3)

        _min = min(take1step, take2step, take3step)
        dp[index] = _min + jumps[index]
    return dp[index]


def main():

  print(find_min_fee([1, 2, 5, 2, 1, 2]))
  print(find_min_fee([10, 15, 20]))


main()