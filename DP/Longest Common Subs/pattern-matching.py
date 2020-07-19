
def find_SPM_count(str, pat):
    s, p = len(str), len(pat)
    if p == 0:
        return 1
    
    if p > s or s == 0:
        return 0
    
    dp = [[0 for _ in range(p+1)] for _ in range(s+1)]

    for i in range(s+1):
        dp[i][0] = 1
    
    for i in range(1, s+1):
        for j in range(1, p+1):
            if str[i-1] == pat[j-1]:
                dp[i][j] = dp[i-1][j-1]
            dp[i][j] += dp[i-1][j]
    return dp[s][p]









def main():
  print(find_SPM_count("baxmx", "ax"))
  print(find_SPM_count("tomorrow", "tor"))


main()