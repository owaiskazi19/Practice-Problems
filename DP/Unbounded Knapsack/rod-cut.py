
def solve_rod_cutting(lengths, price, rod_length):
  dp = [[-1 for x in range(rod_length+1)] for y in range(len(lengths))]
  return check_rods(dp, lengths, price, rod_length, 0)

def check_rods(dp, lengths, price, rod_length, index):
  n = len(price)

  if len(lengths) != len(price) or n == 0 or index >= n or rod_length <= 0:
    return 0

  if dp[index][rod_length] == -1:
    profit1 = 0
    if lengths[index] <= rod_length:
      profit1 = price[index] + check_rods(dp, lengths, price, rod_length - lengths[index], index)
    
    profit2 = check_rods(dp, lengths, price, rod_length, index + 1)

    dp[index][rod_length] = max(profit1, profit2)
  
  return dp[index][rod_length]














def main():
  print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()