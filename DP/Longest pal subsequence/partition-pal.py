
def find_MPP_cuts(s):
    n = len(s)

    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
    
    for end in range(1, n):
        for start in range(end - 1, -1, -1):
            if s[start] == s[end]:
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
    

    cuts = [0 for _ in range(n)]
    for i in range(n):
        temp = n
        if dp[0][i]:
            cuts[i] = 0
        else:
            for j in range(i):
                if dp[j+1][i] and temp > cuts[j] + 1:
                    temp = cuts[j] + 1
            cuts[i] = temp
    print cuts
    return cuts[n-1]




def main():
  print(find_MPP_cuts("abdbca"))
  print(find_MPP_cuts("cdpdd"))
  print(find_MPP_cuts("pqr"))
  print(find_MPP_cuts("pp"))
  print(find_MPP_cuts("madam"))


main()