def binarySearch(arr, low, high, n):
    
    
    while low <=high:
        mid = low + (high-low)/2
        if arr[mid] == 1 and (arr[mid-1] != 1 or mid == 0):
            return n - mid
        elif arr[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1


arr = [0, 0, 0, 0, 1, 1, 1, 1, 1]
ans = binarySearch(arr, 0, len(arr)-1, len(arr))
print ans 

# O(logn)