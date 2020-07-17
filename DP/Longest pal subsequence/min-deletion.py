

def find_LPS_length(s):
    n = len(s)

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    
    for end in range(1, n):
        for start in range(end-1,-1,-1):
            if s[start] == s[end]:
                dp[start][end] = 2 + dp[start+1][end-1]
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    

    return len(s) - dp[0][n-1]



def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()