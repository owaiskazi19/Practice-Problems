
def find_LPS_length(s):
    n = len(s)

    dp = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        dp[i][i] = True
        count += 1
    
   
    for end in range(1, n):
        for start in range(end - 1, -1, -1):
            if s[start] == s[end]:
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    count += 1


    return count



def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()