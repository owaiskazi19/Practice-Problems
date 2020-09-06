# def Fibo(n):
#     if n <=1:
#         return n
    
#     return Fibo(n-1) + Fibo(n-2)

# for i in range(10):
#     print Fibo(i)



def fiboo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        f = 0
        f0 = 0
        f1 = 1
        for i in range(2, n+1):
            f = f0 + f1
            f0 = f1
            f1 = f
        return f
    else:
        return -1

for i in range(10):
    print fiboo(i)
