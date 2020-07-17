
def find_LPS_length(s):
    n = len(s)
    dp = [[-1 for x in range(n)] for y in range(n)]
    check_LPS(dp, s, 0, n - 1, 0 , 0)
    print (palStart, palEnd)

def check_LPS(dp, s, start, end, palStart, palEnd):
    if start > end:
        return 0
    
    if start == end:
        return 1
    
    if dp[start][end] == -1:
        if s[start] == s[end]:
            remainingLength = end - start - 1

            if remainingLength == check_LPS(dp, s, start + 1, end - 1, palStart, palEnd):
                dp[start][end] =  remainingLength + 2
                return dp[start][end]
    
        c1 = check_LPS(dp, s, start + 1, end, palStart, palEnd)
        c2 = check_LPS(dp, s, start, end - 1, palStart, palEnd)

        dp[start][end] = max(c1, c2)
    

    return dp[start][end]






def main():

  print(find_LPS_length("abdbca"))
  #print(find_LPS_length("cddpd"))
  #print(find_LPS_length("pqr"))

#res = []
palStart = 0
palEnd = 0
main()