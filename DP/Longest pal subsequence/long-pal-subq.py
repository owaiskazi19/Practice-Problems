
def find_LPS_length(seq):
    n = len(seq)
    dp = [[-1 for x in range(n)] for y in range(n)]
    return check_LPS(dp, seq, 0, n-1)

def check_LPS(dp, seq, start, end):
    if start > end:
        return 0
    
    if start == end:
        return 1
    
    if dp[start][end] == -1:
        if seq[start] == seq[end]:
            dp[start][end] = 2 + check_LPS(dp, seq, start + 1, end - 1)
        else:
            c1 = check_LPS(dp, seq, start + 1, end)
            c2 = check_LPS(dp, seq, start, end - 1)
            dp[start][end] = max(c1, c2)
    
    return dp[start][end]
        











def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()