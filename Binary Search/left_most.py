def binarySearch(arr, k, low, high):
    
    
    while low <=high:
        mid = low + (high-low)/2
        if arr[mid] == k and (arr[mid-1] != k or mid == 0):
            return mid
        elif arr[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1


arr = [2,3,3,3,3]
k = 3
ans = binarySearch(arr, k, 0, len(arr)-1)
print ans

# O(logn)