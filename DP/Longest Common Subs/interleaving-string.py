

def find_SI(m,n,p):
    return check_Interative({}, m , n , p, 0, 0, 0)

def check_Interative(dp, m, n, p, mIn, nIn, pIn):
    
    mLen, nLen, pLen = len(m), len(n), len(p)

    if mLen == mIn and nLen == nIn and pLen == pIn:
        return True

    if pLen == pIn:
        return False

    subPro = str(mIn) + '-' + str(nIn) + '-' + str(pIn)

    if subPro not in dp:
        b1, b2 = False, False

        if mLen > mIn and m[mIn] == p[pIn]:
            b1 = check_Interative(dp, m, n, p, mIn + 1, nIn, pIn+1)
        
        if nLen > nIn and n[nIn] == p[pIn]:
            b2 = check_Interative(dp, m, n, p, mIn, nIn + 1, pIn+1)
        
        dp[subPro] = b1 or b2
    
    
    return dp[subPro]



def main():
  print(find_SI("abd", "cef", "abcdef"))
  print(find_SI("abd", "cef", "adcbef"))
  print(find_SI("abc", "def", "abdccf"))
  print(find_SI("abcdef", "mnop", "mnaobcdepf"))


main()