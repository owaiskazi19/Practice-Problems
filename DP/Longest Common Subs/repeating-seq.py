
def find_LRS_length(s):
    n = len(s)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    maxLength = 0

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j and s[i-1] == s[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            maxLength = max(maxLength, dp[i][j])
    
    return maxLength









def main():
  print(find_LRS_length("tomorrow"))
  print(find_LRS_length("aabdbcec"))
  print(find_LRS_length("fmff"))


main()