def check(arr):
    mn = arr[0]
    mx = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > mx:
            mx = arr[i]
        elif arr[i] < mn:
            mn = arr[i]
    
    return mx,mn





print check([3,4,1,5,7,6])