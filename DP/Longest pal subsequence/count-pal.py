
def count_PS(s):
    n = len(s)
    dp = [[-1 for x in range(n)] for y in range(n)]

    return check_count(dp, s, 0, n - 1, 0)

def check_count(dp, s, start, end, count):
    if start > end:
        return 0
    
    if start == end:
        return 1
    
    if dp[start][end] == -1:
        if s[start] == s[end]:
            remainingLength = end - start - 1
            if remainingLength == check_count(dp, s, start + 1, end - 1, count):
                dp[start][end] = 2 + remainingLength
                res.append(s[start:end+1])
                count += 1
                return count
    
        c1 = check_count(dp, s, start + 1, end, count)
        c2 = check_count(dp, s, start, end - 1, count)
        dp[start][end] = max(c1, c2)
        #res.append(s[start:end+1])
        count += 1
    return count


            











def main():
  print(count_PS("abdbca"))
  print res
#   print(count_PS("cddpd"))
#   print(count_PS("pqr"))
#   print(count_PS("qqq"))

res = []
main()