def calculateFibonacci(n):
    dp = [-1 for x in range(n+1)]
    return checkFibo(dp, n)

def checkFibo(dp, n):
    if n < 2:
        return n
    
    if dp[n] >= 0:
        return dp[n]
    
    dp[n] = checkFibo(dp, n-1) + checkFibo(dp, n-2)

    return dp[n]



def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()